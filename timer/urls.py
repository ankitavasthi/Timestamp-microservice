from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})/(?P<hour>\d{2})-(?P<minute>\d{2})-(?P<second>\d{2})/$', views.display, name='display'),
    url(r'^(?P<id>[0-9]+)/$', views.display1 , name='display1')
]