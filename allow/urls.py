from django.urls import path
from . import views

app_name = 'allow'


urlpatterns = [
    path('', views.home),
    path('articles/', views.articles, name="articles")
]
