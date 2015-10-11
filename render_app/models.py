from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Objects(models.Model):
	title = models.CharField(max_length=200, null=True, blank=True)
	# slug = models.SlugField(unique=True, null=True, blank=True)
	obj_file = models.FileField(upload_to="objectFile")
	coordinates = models.CharField(max_length=500000, null=True, blank=True)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = ("Object")
		verbose_name_plural = ("Objects")

	# def save(self, *args, **kwargs):
	# 	self.slug = slugify(self.title)
	# 	super(Objects, self).save(*args, **kwargs)