from django.contrib.gis.db import models
from thumbs import ImageWithThumbsField

class Heritage(models.Model):
  sr_no = models.CharField(max_length=255, blank=True, null=True, db_index=True)
  asset = models.CharField(max_length=255, blank=True, null=True)
  asset_type = models.CharField(max_length=255, blank=True, null=True)
  location = models.CharField(max_length=255, blank=True, null=True)
  ownership = models.CharField(max_length=255, blank=True, null=True)
  YrOfEst = models.CharField(max_length=255, blank=True, null=True)
  value_clas = models.CharField(max_length=255, blank=True, null=True)
  grade = models.CharField(max_length=255, blank=True, null=True)
  condition = models.CharField(max_length=255, blank=True, null=True)
#  meta_surveyno = models.CharField("Survey No", blank=True, null=True)
  hist_trans = models.TextField("Historical Transformations (if any)", blank=True, null=True)
  hist_patron = models.CharField("Patron", max_length=255, blank=True, null=True)
  hist_architect = models.CharField("Architect", max_length=255, blank=True, null=True)
  hist_context = models.TextField("Social - Economic - Political Context and Significance", blank=True, null=True)
  poly = models.MultiPolygonField() 
  objects = models.GeoManager()

  def __unicode__(self):
    return self.sr_no + " " + self.asset

class HeritageImage(models.Model):
  hid = models.ForeignKey(Heritage)
  img = ImageWithThumbsField(upload_to="images", sizes=((125,125),(200,200)), height_field='height', width_field='width')  
  caption = models.TextField(blank=True)

class MunicipalBoundary(models.Model):
  mn_id = models.IntegerField()
  layer = models.CharField(max_length=255, blank=True, null=True)
  color = models.IntegerField(blank=True, null=True)
  municipali = models.CharField(max_length=255, blank=True, null=True)
  thickness = models.IntegerField(blank=True, null=True)
  handle = models.CharField(max_length=255, blank=True, null=True)
  elevation = models.IntegerField(blank=True, null=True)
  lineweight = models.IntegerField(blank=True, null=True)
  linewidth = models.IntegerField(blank=True, null=True)
  poly = models.MultiPolygonField(blank=True, null=True)
  objects = models.GeoManager()
  
  def __unicode__(self):
    return self.layer

class VillageBoundary(models.Model):
  vlg_id = models.IntegerField()
  layer = models.CharField(max_length=255, blank=True, null=True)
  village_name = models.CharField(max_length=255, blank=True, null=True)
  poly = models.MultiPolygonField(blank=True, null=True)
  objects = models.GeoManager()

  def __unicode__(self):
    return self.village_name

