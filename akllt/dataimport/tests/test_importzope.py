from django.test import TestCase
from django.core.management import call_command

from wagtail.wagtailcore.models import Page

from akllt.dataimport.tests.utils import fixture


class ImportZopeCommandTests(TestCase):
    def test_command(self):
        self.assertEqual(Page.objects.count(), 2)
        call_command('akllt_importzope', fixture('whole_export'), verbosity=0)
        self.assertEqual(Page.objects.count(), 22)