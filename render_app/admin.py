from django.contrib import admin
from models import Objects

# Register your models here.
class ObjectsAdmin(admin.ModelAdmin):
	model = Objects

admin.site.register(Objects, ObjectsAdmin)