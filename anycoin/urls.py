from django.contrib import admin, sitemaps
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.generic import TemplateView
from anycoin.sitemaps import StaticViewSitemap
from .sitemaps import StaticViewSitemap


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('crypto.urls')),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

sitemaps = {'static': StaticViewSitemap,
            }
