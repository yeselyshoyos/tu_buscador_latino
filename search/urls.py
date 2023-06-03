from django import views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path("", views.Search, name="search"),
    path("report", views.Report, name="report"),

    # Routes with django rest framework
    path("save_searches", csrf_exempt(views.save_searches)),
    path("create_report", csrf_exempt(views.create_report), name="create-report"),
]