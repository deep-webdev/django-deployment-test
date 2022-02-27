from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='home'),
    path("users/", views.users, name="users"),
    path("form/", views.form_name_view, name="form"),
    path("new_user_form/", views.new_user_form, name="New User Form"),
    path("other/", views.other, name="other"),
    path("relative/", views.relative, name="relative")
]