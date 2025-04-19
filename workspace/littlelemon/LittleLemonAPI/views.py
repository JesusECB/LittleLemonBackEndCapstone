#LittleLemonAPI/views.py
from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

class MenuItemView(ListCreateAPIView):
    """
    View for listing all MenuItems (GET) and creating a new MenuItem (POST).
    """
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAuthenticated]
    queryset               = MenuItem.objects.all()
    serializer_class       = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    """
    View for retrieving (GET), updating (PUT) or deleting (DELETE) a single MenuItem instance.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAuthenticated]
    queryset               = MenuItem.objects.all()
    serializer_class       = MenuItemSerializer

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})