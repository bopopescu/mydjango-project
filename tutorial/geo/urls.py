from django.conf.urls import url
from .models import *
from .views import *
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^data/$', GeoJSONLayerView.as_view(model=SeoulPoint, properties=('number','name','juso','latitude','longitude')),name='data'),
    # url(r'^geodata/$', Geo_datasets, name = 'geo_data'),
    # url(r'^incidence_data/$', GeoDjangoView.as_view(), name='home'),
]