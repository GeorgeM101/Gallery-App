from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_image, name='search'),
    path('location/<location>', views.location_view, name='Location')
]
