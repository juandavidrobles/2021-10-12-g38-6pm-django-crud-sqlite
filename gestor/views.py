from django.shortcuts import render
from django.http import JsonResponse
from gestor.models import Article

def hello(request):
  return JsonResponse({
    'ok': True,
    'message': 'Hello'
  })

def add_article_form(request):
  return render(request, 'article-form.html')

def add_article(request, name, category, price):
  Article.objects.create(name=name, category=category, price=price)
  return JsonResponse({
    'ok': True,
    'name': name,
    'category': category,
    'price': price,
  })