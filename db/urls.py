from django.urls import path, include
from . import views

app_name = "db"

urlpatterns = [
    path('', views.index, name="index"),
    path('users/', views.checkusers, name="check")
]