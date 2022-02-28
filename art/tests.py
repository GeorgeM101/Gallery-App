from django.test import TestCase
from art.models import Category, Location, Image
# Create your tests here.

class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='lifestyle')
        self.name = Category(name='lifestyle')

    def test_instance(self):
        self.assertTrue(isinstance(self.name,Category))