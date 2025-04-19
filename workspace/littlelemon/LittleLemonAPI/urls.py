#LittleLemonAPI/urls.py
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('menu-items/', views.MenuItemView.as_view(), name='menu-list'),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
    path('message/', views.msg, name='message'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
