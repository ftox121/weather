from django.test import TestCase, Client
from django.urls import reverse

class SearchFormTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_search_form_get(self):
        response = self.client.get(reverse('weatherapp:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Enter city')

    def test_search_form_post(self):
        response = self.client.post(reverse('weatherapp:home'), {'city': 'Moscow'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Moscow')