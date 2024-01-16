from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import EditProfileView, RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path(
        "login/",
        LoginView.as_view(template_name="authentication/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="authentication/logout.html"),
        name="logout",
    ),
    path(
        "edit_profile/",
        EditProfileView.as_view(template_name="authentication/edit_profile.html"),
        name="edit_profile",
    ),
]
