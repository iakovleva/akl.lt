import tqdm

from django.core.management.base import BaseCommand

from wagtail.wagtailcore.models import Page

import akllt.dataimport.news  as newsparser
from akllt.news.models import NewsStory


class Command(BaseCommand):
    args = '<directory name>'
    help = 'Imports data from old akl.lt website'

    def handle(self, news_folder, *args, **options):
        verbosity = int(options['verbosity'])
        news_count = 0
        root = Page.get_first_root_node()
        if root is None:
            root = Page.add_root(title='Root page')

        if verbosity > 1:
            files = newsparser.iter_news_files(news_folder)
        else:
            files = tqdm.tqdm(list(newsparser.iter_news_files(news_folder)))

        for path in files:
            if verbosity > 1:
                self.stdout.write(str(path))
            try:
                news_item = newsparser.parse_metadata(path)
                root.add_child(instance=NewsStory(
                    title=news_item['title'],
                    date=news_item['date'],
                    blurb=news_item['blurb'],
                    body=news_item['body'],
                ))
            except:
                self.stdout.write(
                    '\n\nError occured while importing %s news file.' % path
                )
                raise
            news_count += 1

        self.stdout.write('Successfully imported %d news items\n' % news_count)
