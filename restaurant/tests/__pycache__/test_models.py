# restaurant/tests/test_models.py
from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        # DecimalField outputs with 2 decimals, so adjust expected string
        self.assertEqual(str(item), "IceCream : 80.00")
