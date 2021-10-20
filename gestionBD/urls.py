"""gestionBD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestionBD.views import add_article, admin_articles, admin_root

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello/', hello),
    # path('form-article/', add_article_form),
    # path('add-article/<str:name>/<str:category>/<int:price>/', add_article),
    path('admin-panel/', admin_root),
    path('admin-panel/articles/', admin_articles),
    # API
    path('api/add-article/', add_article),
]
