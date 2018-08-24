from django.test import TestCase
from django.test import Client
from .models import Orders
from django.core.serializers import serialize


class TestGetOrderByID(TestCase):
    def setUp(self):
        self.client = Client()
        self.id = 66996325

    def prepare_expected(self):
        order = Orders.objects.get(internal_id=self.id)
        order_record = serialize('json', [order, ])
        order_record = str(order_record).replace('\"', '\'')
        return str(order_record).replace('null', 'None')

    def test_get_valid_order_record(self):
        Orders.objects.create(index=1, internal_id=self.id)
        response = self.client.get(f'/orders/{self.id}/')
        expected = self.prepare_expected()
        self.assertEqual(str(response.json()), expected)
        self.assertEqual(response.status_code, 200)

    def test_get_invalid_single_puppy(self):
        fake_id = 66996326
        response = self.client.get(f'/orders/{fake_id}/')
        self.assertEqual(response.status_code, 404)
