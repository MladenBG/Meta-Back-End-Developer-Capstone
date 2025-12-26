from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create test data
        self.item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.item2 = Menu.objects.create(title="Pizza", price=120, inventory=50)

    def test_get_all_menu_items(self):
        # Call the API endpoint
        url = reverse('menu-list')  # make sure your urls.py has a name='menu-list'
        response = self.client.get(url)

        # Serialize the data for comparison
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_menu_item(self):
        url = reverse('menu-detail', args=[self.item1.id])  # name='menu-detail' in urls.py
        response = self.client.get(url)

        serializer = MenuSerializer(self.item1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
