# tests/test_views.py

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer  # Asegúrate de importar el serializador correcto
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='prueba123')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Crear algunos elementos del menú para las pruebas
        Menu.objects.create(title="IceCream", price=80.00, inventory=100)
        Menu.objects.create(title="Pizza", price=150.00, inventory=50)
        Menu.objects.create(title="Pasta", price=120.00, inventory=30)


    def test_getall(self):
        # Hacer una solicitud GET a la vista del menú
        response = self.client.get('/api/menu/')  # Ajusta la URL de acuerdo con tu configuración de urls.py

        # Recuperar todos los objetos del menú
        menu_items = Menu.objects.all()

        # Serializar los datos del menú
        serializer = MenuSerializer(menu_items, many=True)

        # Verificar que la respuesta de la API sea exitosa
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificar que la respuesta de la API contenga los datos correctos
        self.assertEqual(response.data, serializer.data)
