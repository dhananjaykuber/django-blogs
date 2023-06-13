from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all().order_by("date")
    return render(request, "blogs/blog_list.html", {"blogs": blogs})


def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "blogs/blog_detail.html", {"blog": blog})


@login_required(login_url="/accounts/login/")
def create_blog(request):
    if request.method == "POST":
        form = forms.CreateBlog(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("blogs:blog_list")

    else:
        form = forms.CreateBlog()

    return render(request, "blogs/create_blog.html", {"form": form})
