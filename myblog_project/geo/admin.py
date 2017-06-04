from django.contrib import admin
from .models import *
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
# class ElectionereaAdmin(LeafletGeoAdmin):
#     list_display = ('objectid','선거', 'shape_leng', 'shape_area' )
#
# admin.site.register(ElectionsErea, ElectionereaAdmin)

class SeoulpointAdmin(LeafletGeoAdmin):
    list_display = ('number','name','juso','latitude','longitude','geom')


admin.site.register(SeoulPoint, SeoulpointAdmin)