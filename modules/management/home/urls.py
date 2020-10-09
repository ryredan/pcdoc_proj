from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .forms import LoginForm

urlpatterns = [
    path('', views.Dashboard.as_view(), name="dashboard"),
    path('login/', LoginView.as_view(template_name = 'registration/login.html', form_class = LoginForm), name="login"),
    path('logout', LogoutView.as_view(), name="logout")
]