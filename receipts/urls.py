from django.urls import path
from django.shortcuts import redirect

from . import views

urlpatterns = [
    path('', views.receipts, name='receipts'),
    path('details/<int:receipt_id>/', views.details, name='receipt_details'),
    path('create/', views.create, name='create_receipt'),
    path('create/<str:workplace_uuid>/', views.create, name='create_receipt_with_params'),
    path('delete/', views.delete, name='delete_receipt'),
    path('update/<str:receipt_id>/', views.update, name='update_receipt'),
    path('<str:workplace_uuid>/<int:page_num>/', views.receipts, name='receipts_with_params'),
]
