"""brs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from apps.books import views

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^admin/', include('apps.admin.urls', namespace='admin')),
    url(r'^users/', include('apps.users.urls', namespace='users')),
    url(r'^categories/', include('apps.categories.urls', namespace='categories')),
    url(r'^books/', include('apps.books.urls', namespace='books')),
    url(r'^requests/', include('apps.requestbooks.urls', namespace='requests')),
]