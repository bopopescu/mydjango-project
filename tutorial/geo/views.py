# from django.shortcuts import render, HttpResponse
# from .models import ElectionErea
# from django.views.generic import TemplateView
# from django.core.serializers import serialize
# from django.http import HttpResponse
# # Create your views here.
#
# class GeoDjangoView(TemplateView):
#     template_name = 'index.html'
#
# def Geo_datasets(request):
#     geo = serialize('geojson', ElectionErea.objects.all() )
#     return HttpResponse(geo, content_type="json")