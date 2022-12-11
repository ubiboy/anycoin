from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return [
            'home',
            'prices',
        ]

    def location(self, item):
        return reverse(item)
