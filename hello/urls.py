from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("profile/", views.uprofile, name="profile"),
    path("settings/", views.settings, name="settings"),
    path("login/", auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path("templates1/", views.templates1, name="templates1"),
    path("templates2/", views.templates2, name="templates2"),
    path("templates3/", views.templates3, name="templates3"),
    path("start/", views.start, name="start"),
    path("stop/", views.stop, name="stop"),

]