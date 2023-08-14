from django.shortcuts import render, redirect
from .models import Tweet


# Create your views here.


def index(request):

    return render(request, 'tweets/index.html')


def timeline(request):
    tweet_list = Tweet.objects.all()
    return render(request, 'tweets/timeline.html', {'tweet_list': tweet_list})