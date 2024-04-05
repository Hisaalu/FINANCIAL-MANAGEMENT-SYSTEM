from django.urls import path
from . import views

urlpatterns = [
    path('', views.tables, name='tables'),
    path('details/<int:table_id>/', views.details, name='table_details'),
    path('create/', views.create, name='create_table'),
    path('create/<str:workplace_uuid>/', views.create, name='create_table_with_params'),
    path('delete/', views.delete, name='delete_table'),
    path('update/<int:table_id>/', views.update, name="update_table"),
    path('<str:workplace_uuid>/<int:page_num>/', views.tables, name='tables_with_params'),
]
