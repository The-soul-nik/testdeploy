from django.shortcuts import render
from .models import Article
# Create your views here.


def home(request):
    return render(request, 'allow/home.html',)


def articles(request):
    articles = Article.objects.all()
    return render(request, 'allow/articles.html', {'articles':articles})
