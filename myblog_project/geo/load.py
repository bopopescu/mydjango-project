import os
from django.contrib.gis.utils import LayerMapping
from .models import *

# electionserea_mapping = {
#     'objectid' : 'OBJECTID',
#     '선거' : '선거',
#     'shape_leng' : 'Shape_Leng',
#     'shape_area' : 'Shape_Area',
#     'geom' : 'MULTIPOLYGON',
# }
#
# election_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/선거구20대.shp'))
#
# def run(verbose=True):
#     ours = LayerMapping(ElectionsErea, election_shp, electionserea_mapping
#                         , transform=False)
#     ours.save(strict=True, verbose=verbose)

seoulpoint_mapping = {
    'latitude':'Latitude',
    'longitude':'Longitude',
    'number':'number',
    'juso':'juso',
    'name':'name',
    'geom':'POINT',
}

seoulpoint_shp= os.path.abspath(os.path.join(os.path.dirname(__file__),'data/point3.shp'))
def run(verbose=True):
    ours = LayerMapping(SeoulPoint, seoulpoint_shp, seoulpoint_mapping, transform=False)
    ours.save(strict=False, verbose=verbose)

