from akllt.news.models import NewsIndex
from akllt.news.models import NewsStory

from akllt.dataimport.importers.base import BaseImporter
from akllt.dataimport.importers.base import ImportItem


class NewsImporter(BaseImporter):
    page_class = NewsStory
    root_page_class = NewsIndex

    def iterate_paths(self):
        for path in self.path.iterdir():
            if path.name.startswith('naujiena_'):
                yield ImportItem(path=path)

    def prepare_page_instance(self, instance, item, data):
        super(NewsImporter, self).prepare_page_instance(instance, item, data)
        instance.blurb = self.parse_content(item.path, data['blurb'])
