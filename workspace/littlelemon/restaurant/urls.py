# restaurant/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views as restaurant_views
from . import views

router = DefaultRouter()
router.register(r'tables', restaurant_views.BookingViewSet)

urlpatterns = [
    path('booking/', include(router.urls)),
    path('', restaurant_views.index, name='index'),
    path('api/menu/', restaurant_views.MenuItemView.as_view(), name='menu-list'),
    path('api/menu/<int:pk>/', restaurant_views.SingleMenuItemView.as_view(), name='menu-detail'),
]
