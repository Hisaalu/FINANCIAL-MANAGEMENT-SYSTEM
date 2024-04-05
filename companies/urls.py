from django.urls import path
from . import views
from django.shortcuts import redirect
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/companies/1/1/')),
    path('<int:workplaces_page_num>/<int:owned_companies_page_num>/', views.companies, name='companies'),
    path('create/', views.create, name='create_company'),
    path('join/', views.join, name='join_company'),
    path('delete/', views.delete, name='delete_company'),
    path('fire/', views.fire_staff, name='fire_employee'),
    path('quit/', views.leave, name='quit_company'),
    path('manage/<str:company_uuid>/', views.render_staff_page, name='manage_staff'),
    path('update/<str:company_uuid>/', views.update_company, name='update_company'),
    path('details/<str:company_uuid>/', views.details, name='company_details'),
]
