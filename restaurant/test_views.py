from django.test import TestCase
from .models import Menu
from .serializers import MenuSerializer
from rest_framework.test import APIClient
from django.urls import reverse
import json


class MenuViewTest(TestCase):
    def setUp(self):
       self.menu = Menu.objects.create(title="Pasta", price=29.99, inventory=70)
        
    def test_getall(self):
        serializer = MenuSerializer(self.menu)
        expected_data = serializer.data
        
        client = APIClient()
        response = client.get(reverse('menu_list'))
        response_data = json.loads(response.content)
        self.assertEqual(response_data, [expected_data])