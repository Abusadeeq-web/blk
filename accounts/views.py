from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login
from accounts.models import User
from .forms import RegisterForm
from django.views.generic import TemplateView
# Create your views here.


class index(TemplateView):
	template_name="index.html"

def landing(request):
	return render(request, 'landing-page.html')
	
def profile(request):
	return render(request, 'accounts/profile-page.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            messages.success(request, f"you're welcome to ")
            return redirect('profile')
            return render(request, 'accounts/profile-page.html', context )
    else:
        form = RegisterForm()
    return render(request, 'accounts/signup.html', {'form':form})