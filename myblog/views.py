from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from myblog.models import Post


@login_required
def home(request):
    return render(request, 'myblog/home.html', {'posts': Post.objects.all()})


@login_required
def about(request):
    return render(request, 'myblog/about.html')
