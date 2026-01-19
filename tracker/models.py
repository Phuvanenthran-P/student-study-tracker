from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone


class Subject(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="subjects"
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"


class StudyPlan(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="study_plans"
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="study_plans"
    )
    daily_target_hours = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-start_date"]

    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError("End date cannot be before start date.")

        if self.daily_target_hours <= 0:
            raise ValidationError("Daily target hours must be greater than zero.")

        # Prevent overlapping active plans for same subject & user
        if self.is_active:
            qs = StudyPlan.objects.filter(
                user=self.user,
                subject=self.subject,
                is_active=True
            ).exclude(pk=self.pk)

            if qs.exists():
                raise ValidationError(
                    "An active study plan already exists for this subject."
                )

    def __str__(self):
        return f"Plan for {self.subject.name} ({self.daily_target_hours} hrs/day)"


class StudyLog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="study_logs"
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="study_logs"
    )
    study_date = models.DateField()
    hours_spent = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-study_date"]
        unique_together = ("user", "subject", "study_date")

    def clean(self):
        if self.hours_spent <= 0:
            raise ValidationError("Hours spent must be greater than zero.")

        if self.study_date > timezone.now().date():
            raise ValidationError("Study date cannot be in the future.")

    def __str__(self):
        return f"{self.subject.name} - {self.study_date} ({self.hours_spent} hrs)"
