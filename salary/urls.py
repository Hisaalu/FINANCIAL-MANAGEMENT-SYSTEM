from django.urls import path
from . import views

urlpatterns = [
    path('', views.salary, name='salary'),
    path('details/<int:salary_id>/', views.details, name='salary_details'),
    path('create/', views.create, name='create_salary'),
    path('create/<str:company_uuid>/', views.create, name='create_salary_with_params'),
    path('delete/', views.delete, name='delete_salary'),
    path('update/<int:salary_id>/', views.update, name="update_salary"),
    path('<str:company_uuid>/<int:page_num>/', views.salary, name='salary_with_params'),
]
