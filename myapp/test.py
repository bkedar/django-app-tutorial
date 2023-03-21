from django.test import TestCase, Client


class MyappTestCase(TestCase):

    def test_hello_view(self):
        client = Client()
        response = client.get('/hello/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Hello, world!")
