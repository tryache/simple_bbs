from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import logging

logger = logging.getLogger("django.request")


class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return redirect("/posts")
        else:
            return render(request, "index.html")


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return redirect("/posts")
        else:
            return render(request, "login.html")

    def post(self, request):
        user_id = request.POST['user_id']
        password = request.POST['password']
        user = authenticate(username=user_id, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect("/posts")
        else:
            return redirect("/login")


class RegisterView(View):
    def post(self, request):
        logger.info(request.POST)
        try:
            user_id = request.POST['user_id']
            password = request.POST['password']
            logger.error("register failed")
            user = User.objects.create_user(user_id, request.POST['email'], password)
            user.save()
            user_auth = authenticate(username=user_id, password=password)
            login(request, user_auth)
            return redirect("/posts")
        except Exception:
            return redirect("/")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/login")