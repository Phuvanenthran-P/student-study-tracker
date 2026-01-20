from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SubjectForm, StudyPlanForm, StudyLogForm
from .models import Subject, StudyPlan, StudyLog
from django.db.models import Sum
from datetime import date, timedelta


@login_required
def dashboard(request):
    user = request.user
    subjects = user.subjects.all()
    logs = user.study_logs.all()

    # Weekly summary
    week_ago = date.today() - timedelta(days=7)
    weekly_logs = logs.filter(study_date__gte=week_ago)
    weekly_summary = weekly_logs.values('subject__name').annotate(total_hours=Sum('hours_spent'))

    context = {
        'subjects': subjects,
        'weekly_summary': weekly_summary,
    }
    return render(request, 'tracker/dashboard.html', context)


@login_required
def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.user = request.user
            subject.save()
            return redirect('dashboard')
    else:
        form = SubjectForm()
    return render(request, 'tracker/form.html', {'form': form, 'title': 'Add Subject'})


@login_required
def add_study_plan(request):
    if request.method == 'POST':
        form = StudyPlanForm(request.POST, user=request.user)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.user = request.user
            plan.save()
            return redirect('dashboard')
    else:
        form = StudyPlanForm(user=request.user)

    return render(request, 'tracker/add_study_plan.html', {'form': form})

@login_required
def add_study_log(request):
    if request.method == 'POST':
        form = StudyLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            log.full_clean()
            log.save()
            return redirect('dashboard')
    else:
        form = StudyLogForm()
    return render(request, 'tracker/form.html', {'form': form, 'title': 'Add Study Log'})
