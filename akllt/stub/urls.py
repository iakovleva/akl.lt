from django.conf.urls import patterns, url


urlpatterns = patterns(
    'akllt.stub.views',
    url(r'^wiki', 'wiki', name='wiki'),
)
