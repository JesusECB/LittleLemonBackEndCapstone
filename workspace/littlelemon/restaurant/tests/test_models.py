# tests/test_models.py

from django.test import TestCase
from restaurant.models import Menu  # Asegúrate de importar el modelo correcto

class MenuTest(TestCase):
    def test_get_item(self):
        # Crear un objeto MenuItem
        item = Menu.objects.create(title="IceCream", price=80.00, inventory=100)

        # Verificar que la representación en cadena sea correcta
        self.assertEqual(str(item), "IceCream : 80.00")
