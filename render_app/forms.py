from django import forms

from models import Objects

class ObjectsForm(forms.ModelForm):
	class Meta:
		model = Objects
		fields = ('title', 'obj_file', 'coordinates') # , 'cover_photo', 'texture'
		widgets = {
			'title': forms.TextInput(attrs={"class": "form-control", "type": "text", "placeholder": "Name of your 3D Object"}),
			# 'cover_photo': forms.FileInput(attrs={"id": "input-20", "type": "file", "class": "file-loading"}),
			# 'texture': forms.FileInput(attrs={"id": "input-21", "type": "file", "class": "file-loading"}),
			'obj_file': forms.FileInput(attrs={"id": "input-22", "type": "file", "class": "file-loading"}),
		}