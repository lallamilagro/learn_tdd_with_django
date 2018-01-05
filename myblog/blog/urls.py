from django.conf.urls import urls

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.EntryDetail.as_view(), name='entry_detail'),
]