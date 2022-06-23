from django.test import TestCase

from .models import *


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='boni', password='!@#haojue')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()


class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='boni')
        self.post = Neighborhoods_cool.objects.create(
            id=1, title='test post', photo='https://res.cloudinary.com/twin221/image/upload/v1655229303/w4mhd4zzdaobfr5dbjwh.png', description='noma',
            user=self.user, url='https://github.com/bonface221')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Neighborhoods_cool))

    def test_save_post(self):
        self.post.save_post()
        post = Neighborhoods_cool.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        posts = Neighborhoods_cool.all_posts()
        self.assertTrue(len(posts) > 0)

    def test_search_post(self):
        self.post.save()
        post = Neighborhoods_cool.search_project('test')
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Neighborhoods_cool.search_project('test')
        self.assertTrue(len(post) < 1)

