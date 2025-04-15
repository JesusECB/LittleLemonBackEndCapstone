from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

def index(request):
    return render(request, 'index.html', {})

class BookingViewSet(viewsets.ModelViewSet):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class MenuItemView(generics.ListCreateAPIView):
    """
    Esta vista maneja los métodos GET y POST para el modelo Menu:
    - GET: Listar todos los elementos del menú.
    - POST: Crear un nuevo elemento del menú.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    """
    Esta vista maneja los métodos GET, PUT y DELETE para un solo elemento del menú:
    - GET: Recuperar los detalles de un elemento.
    - PUT: Actualizar un elemento.
    - DELETE: Eliminar un elemento.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
