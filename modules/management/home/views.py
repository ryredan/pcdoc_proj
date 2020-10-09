from django.views.generic.base import View
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate

   
class Dashboard(LoginRequiredMixin, View):
    login_url = 'login/'
    def get(self, request):
        return render(request, 'index.html')


