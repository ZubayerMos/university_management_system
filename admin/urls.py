from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('adminLogin/', views.admin_login, name='admin_login'),
    path('adminRegister/', views.admin_register, name='admin_register'),
]
