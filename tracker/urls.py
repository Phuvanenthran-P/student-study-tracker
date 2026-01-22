from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("subject/add/", views.add_subject, name="add_subject"),
    path("plan/add/", views.add_study_plan, name="add_study_plan"),
    path("plan/delete/<int:pk>/", views.delete_study_plan, name="delete_study_plan"),
    path("log/add/", views.add_study_log, name="add_study_log"),
]
