from django.shortcuts import render
from blog.models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, "home/index.html", {"posts": posts})
