from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View

from .forms import CustomUserChangeForm


class RegisterView(View):
    template_name = "authentication/register.html"
    form_class = UserCreationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
        return render(request, self.template_name, {"form": form})


class CustomLoginView(LoginView):
    template_name = "authentication/login.html"
    success_url = reverse_lazy("index")


class EditProfileView(View):
    template_name = "edit_profile.html"
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("index")

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен.")
            return render(
                request, self.template_name, {"form": form, "redirect_delay": 1}
            )
        return render(request, self.template_name, {"form": form})


class LogoutView(View):
    template_name = "logout.html"

    def post(self, request, *args, **kwargs):
        logout(request)
        return render(request, self.template_name)
