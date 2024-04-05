from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='alert_and_redirect.html'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('password/', views.change_password, name='change_password'),
    path('logout/', views.custom_logout, name='logout'),
]
