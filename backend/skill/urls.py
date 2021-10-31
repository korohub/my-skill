from django.conf.urls import url
from django.urls.resolvers import URLPattern
from skill import views

urlpatterns = [
    url(r'^skill$', views.skillApi),
    url(r'^skill/([0-9]+)$',views.skillApi),
    url(r'^details_all$',views.details_all),
    url(r'^details/([a-zA-Z0-9_]+)$',views.detailsApi),
]