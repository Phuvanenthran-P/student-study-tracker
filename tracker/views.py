from datetime import date
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.db import IntegrityError
from .models import Subject, StudyPlan, StudyLog
from .forms import SubjectForm, StudyPlanForm, StudyLogForm


def signup(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.save())
        return redirect("dashboard")
    return render(request, "auth/signup.html", {"form": form})


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("dashboard")
    return render(request, "auth/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard(request):
    plans = StudyPlan.objects.filter(user=request.user)
    today = date.today()
    data = []

    for plan in plans:
        total = StudyLog.objects.filter(
            user=request.user,
            subject=plan.subject,
            date__range=(plan.start_date, today)
        ).aggregate(Sum("hours"))["hours__sum"] or 0

        expected = (today - plan.start_date).days + 1
        expected *= plan.daily_target_hours

        progress = min(int((total / expected) * 100), 100) if expected > 0 else 0

        data.append({
            "plan": plan,
            "total_logged": total,
            "progress": progress
        })

    return render(request, "tracker/dashboard.html", {"dashboard_data": data})


@login_required
def add_subject(request):
    form = SubjectForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect("dashboard")
    return render(request, "tracker/form.html", {"form": form, "title": "Add Subject"})


@login_required
def add_study_plan(request):
    if request.method == "POST":
        form = StudyPlanForm(request.POST, user=request.user)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.user = request.user
            plan.save()
            return redirect("dashboard")
    else:
        form = StudyPlanForm(user=request.user)

    return render(request, "tracker/add_study_plan.html", {"form": form})


@login_required
def add_study_log(request):
    form = StudyLogForm(request.POST or None)

    if form.is_valid():
        subject = form.cleaned_data["subject"]
        date_ = form.cleaned_data["date"]
        hours = form.cleaned_data["hours"]

        log, created = StudyLog.objects.update_or_create(
            user=request.user,
            subject=subject,
            date=date_,
            defaults={"hours": hours},
        )

        return redirect("dashboard")

    return render(
        request,
        "tracker/form.html",
        {"form": form, "title": "Add Study Log"},
    )


@login_required
def delete_study_plan(request, pk):
    StudyPlan.objects.filter(pk=pk, user=request.user).delete()
    return redirect("dashboard")
