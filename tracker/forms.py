from django import forms
from .models import StudyPlan, Subject, StudyLog

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'description']

class StudyPlanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    start_date = forms.DateField(
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(attrs={'placeholder': 'DD-MM-YYYY'})
    )
    end_date = forms.DateField(
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(attrs={'placeholder': 'DD-MM-YYYY'})
    )

    class Meta:
        model = StudyPlan
        fields = ['subject', 'daily_target_hours', 'start_date', 'end_date', 'is_active']


class StudyLogForm(forms.ModelForm):
    study_date = forms.DateField(
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(attrs={'type': 'text', 'placeholder': 'DD-MM-YYYY'})
    )

    class Meta:
        model = StudyLog
        fields = ['subject', 'study_date', 'hours_spent', 'notes']
