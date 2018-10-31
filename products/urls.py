from django.conf.urls import url
from .views import (
    ProductListView,
    #ProductDetailView,
    ProductDetailSlugView,
    #ProductFeaturedListView,
    #ProductFeaturedDetailView
    )

urlpatterns = [
    url(r'^$',ProductListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$',ProductDetailSlugView.as_view(), name='detail'),

    # url(r'^products/(?P<pk>\d)$',ProductDetailView.as_view()),
    #url(r'^featured/$', ProductFeaturedListView.as_view()),
    #url(r'^featured/(?P<pk>\d)$', ProductFeaturedDetailView.as_view()),
]
