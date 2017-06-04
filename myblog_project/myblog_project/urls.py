"""myblog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from blog import urls as blogurls
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from geo import urls as geourls

sitemaps = {
    'posts':PostSitemap,
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include(blogurls.urlpatterns, namespace='blog', app_name='blog')),
    url(r'^sitemap\.xml$',sitemap, {'sitemaps':sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^geo/', include(geourls.urlpatterns, namespace='geo')),
]