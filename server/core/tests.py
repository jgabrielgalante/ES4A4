from django.test import TestCase

from . import models

# Create your tests here.
class SlugTestCase(TestCase):
    def test_gen_slug(self):
        self.assertEqual(models.gen_slug('Sanctus dominus'), 'sanctus-dominus')

