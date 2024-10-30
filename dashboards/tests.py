# in dashboards/tests.py
from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        # This method runs before each test
        Post.objects.create(
            title="Web task",
            ticketsdtails="this is details",
            comment="this is comment",
            piority="medium",
            Duedate="2024-11-01"
        )

    def test_post_creation(self):
        """Test that a Post object is created with correct fields"""
        post = Post.objects.get(title="Web task")
        self.assertEqual(post.ticketsdtails, "this is details")
        self.assertEqual(post.piority, "medium")
        self.assertEqual(post.comment, "this is comment")

