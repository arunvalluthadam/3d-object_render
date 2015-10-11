from django import forms

from models import Objects

class ObjectsForm(forms.ModelForm):
	class Meta:
		model = Objects
		fields = ('title', 'obj_file', 'coordinates')
		widgets = {
			'title': forms.TextInput(attrs={"class": "form-control", "type": "text", "placeholder": "Name of your 3D Object"}),
			'obj_file': forms.FileInput(attrs={"id": "input-20", "type": "file", "class": "file-loading"}),
		}