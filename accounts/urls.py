from django.urls import path
from .views import index,register,profile,landing
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('index/', index, name="index"),
    path('register/', register, name="register"),
    path('login/', LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('profile/', profile, name="profile"),
    path('landing/', landing, name="landing"),
]