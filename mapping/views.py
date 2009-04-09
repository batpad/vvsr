from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.gis.shortcuts import render_to_kml
from django.http import HttpResponse, HttpRequest
from django.utils import simplejson
from django.core import serializers
from mapping.models import  *


def all_kml(request):
     locations  = Heritage.objects.kml()
     return render_to_kml("placemarks.kml", {'places' : locations})

def show_map(request):
  rDict = {}
  count = Heritage.objects.all().count()
  rDict['location_count'] = count
  return render_to_response("olbase.html", {'location_count': rDict})
# Create your views here.

def getObjJson(request):
  sr_no = request.GET['sr']
  obj = get_object_or_404(Heritage, sr_no__iexact=sr_no)
  images = HeritageImage.objects.filter(hid=obj)
  r = {}
  r['sr_no'] = obj.sr_no
  r['asset'] = obj.asset
  r['asset_type'] = obj.asset_type
  r['location'] = obj.location
  r['ownership'] = obj.ownership
  r['YrOfEst'] = obj.YrOfEst
  r['value_clas'] = obj.value_clas
  r['grade'] = obj.grade
  r['condition'] = obj.condition
  r['hist_trans'] = obj.hist_trans
  r['hist_patron'] = obj.hist_patron
  r['hist_architect'] = obj.hist_architect
  r['hist_context'] = obj.hist_context
  r['images'] = []
  inc=0
  for i in images:    
    imagesDict = {}
#    r['images'][inc] = {}
    imagesDict['thumb'] = images[inc].img.url_125x125.replace("http://bombayology.com/", "http://bombayology.com/static/")
    imagesDict['url'] = images[inc].img.url.replace("http://bombayology.com/", "http://bombayology.com/static/")
    r['images'].append(imagesDict)
    inc += 1

#  images = HeritageImage.objects.filter(hid=obj)
#  r['images'] = images
  return HttpResponse(simplejson.dumps(r), mimetype='application/javascript')
