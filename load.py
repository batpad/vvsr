import os
from django.contrib.gis.utils import LayerMapping
from vvsr.mapping.models import Heritage, MunicipalBoundary, VillageBoundary

heritage_mapping = {
    'sr_no' : 'SR__NO',
    'asset' : 'ASSET',
    'asset_type' : 'ASSET_TYPE',
    'location' : 'LOCATION',
    'ownership' : 'OWNERSHIP_',
    'YrOfEst' : 'YR__OF_EST',
    'value_clas' : 'VAULE_CLAS',
    'grade' : 'GRADE',
    'condition' : 'CONDITION',
    'poly' : 'MULTIPOLYGON',
}

heritage_shp = '/home/sanj/vvsr/shp/vvsr test_pol_Heritage_Property_demarcations.shp'

def runHeritage(verbose=True):
    lm = LayerMapping(Heritage, heritage_shp, heritage_mapping,
                      transform=False, encoding='utf-8')
    lm.save(strict=True, verbose=verbose)

municipal_mapping = {
  'mn_id': 'ID',
  'layer': 'LAYER',
  'color': 'COLOR',
  'municipali': 'MUNICIPALI',
  'thickness': 'THICKNESS',
  'handle': 'HANDLE',
  'elevation': 'ELEVATION',
  'lineweight': 'LINEWEIGHT',
  'linewidth': 'LINEWIDTH',
  }

municipal_shp = '/home/sanj/Desktop/warped_linear/municipal_boundaries_warped.shp'

def runMunicipal(verbose=True):
  lm = LayerMapping(MunicipalBoundary, municipal_shp, municipal_mapping, transform=False, encoding='utf-8')
  lm.save(strict=True, verbose=verbose)


village_shp = '/home/sanj/Desktop/warped_linear/village_boundaries_warped.shp'

village_mapping = {
  'vlg_id': 'ID',
  'layer': 'LAYER',
  'village_name': 'VILLAGE_NA',
  }

def runVillage(verbose=True):
  lm = LayerMapping(VillageBoundary, village_shp, village_mapping, transform=False, encoding='utf-8')
  lm.save(strict=True, verbose=verbose)
