from django.urls import path, include
from . import views


urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
]
