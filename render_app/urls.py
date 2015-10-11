from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'render_app.views.home', name='home'),
    url(r'^upload/$', 'render_app.views.upload', name='upload'),
    url(r'^preview/$', 'render_app.views.preview', name='preview'),
    url(r'^gallery-single/(?P<id>[0-9]+)$', 'render_app.views.gallery_single', name='gallery_single'),
    url(r'^gallery/$', 'render_app.views.gallery', name='gallery'),
)
