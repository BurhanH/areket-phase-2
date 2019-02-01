from django.test import TestCase
from django.urls import reverse

from . import models

HTTP_OK = 200


class PostModelTest(TestCase):

    def setUp(self):
        models.Post.objects.create(text='checking post text')

    def test_text_content(self):
        post = models.Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'checking post text')


class HomePageViewTest(TestCase):

    def _check_status_code(self, target, status):
        self.assertEqual(self.client.get(target).status_code, status)

    def setUp(self):
        models.Post.objects.create(text='let\'s check a home page')

    def test_view_url_exist_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTP_OK)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, HTTP_OK)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, HTTP_OK)
        self.assertTemplateUsed(response, 'home.html')
