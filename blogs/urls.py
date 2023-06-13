from django.contrib import admin
from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    path("", views.blog_list, name="blog_list"),
    path("create/", views.create_blog, name="create_blog"),
    path("<slug>/", views.blog_detail, name="blog_detail"),
]
