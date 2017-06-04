from __future__ import unicode_literals
from django.contrib.gis.db import models
# Create your models here.


# class ElectionsErea(models.Model):
#     objectid = models.IntegerField()
#     선거 = models.CharField(max_length=50)
#     shape_leng = models.FloatField()
#     shape_area = models.FloatField()
#     geom = models.MultiPolygonField(srid=21037)
#
#     def __unicode__(self):
#         return self.선거
#
#     class Meta:
#         verbose_name = "Elections"
class SeoulPoint(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    number = models.CharField(max_length=10)
    juso = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    geom = models.PointField(srid=4326, geography=True)

    def __unicode__(self):
        return self.number

    class Meta:
        verbose_name = "Elections"
