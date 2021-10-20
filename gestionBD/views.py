from django.http.response import JsonResponse
from django.shortcuts import render
import json
from gestor.models import Article

def admin_root(request):
  return render(request, 'admin/index.html')

def add_article(request):
  body = json.loads(request.body.decode('utf-8'))
  article = Article(**body)
  article.save()
  print(article.id)
  body['id'] = article.id
  return JsonResponse({
    'ok': True,
    'article': body,
  })

def admin_articles(request):
  articles = get_all_articles()
  return render(request, 'admin/articles.html', {
    'articles': articles,
  })

def get_all_articles():
  return list(Article.objects.values())
