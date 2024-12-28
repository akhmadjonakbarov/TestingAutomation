from unittest import TestCase
from software_testing.blog import Post


class PostTest(TestCase):
    def test_create_post(self):
        # while creating test method, test method should be started with test_something
        post = Post(
            'Test Post',
            'Test Author',
            'Test Description',
        )

        self.assertEqual('Test Post', post.title)
        self.assertEqual('Test Author', post.author)
        self.assertEqual('Test Description', post.content)

    def test_json(self):
        post = Post(
            'Test Post',
            'Test Author',
            'Test Description',
        )
        expected = {
            'title': 'Test Post',
            'author': 'Test Author',
            'content': 'Test Description',
        }
        self.assertDictEqual(expected, post.json())
