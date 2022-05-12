from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user_search/", views.userSearch, name="userSearch"),
    path("users/<user_id>", views.specificUserSearch, name="specificUserSearch"),
]
