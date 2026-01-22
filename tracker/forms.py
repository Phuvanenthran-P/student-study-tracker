from django import forms
from .models import Subject, StudyPlan, StudyLog


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["name"]


class StudyPlanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["subject"].queryset = Subject.objects.filter(user=self.user)

    class Meta:
        model = StudyPlan
        fields = ["subject", "daily_target_hours", "start_date", "end_date", "is_active"]


class StudyLogForm(forms.ModelForm):
    class Meta:
        model = StudyLog
        fields = ["subject", "date", "hours"]
