from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_page, name='index')
]
