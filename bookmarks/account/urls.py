from django.urls import path, include
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
]
