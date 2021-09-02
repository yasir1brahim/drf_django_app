from django.test import TestCase
from .models import User
from .serializers import UserSerializer

class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.user_attributes ={
            'id': 1,
            'first_name': 'Don',
            'last_name': 'Carlos'
        }
        self.user = User.objects.create(**self.user_attributes)
        self.serializer = UserSerializer(instance=self.user)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'first_name', 'last_name']))

    def test_firstName_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['first_name'], self.user_attributes['first_name'])

    def test_lastName_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['last_name'], self.user_attributes['last_name'])