from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import Objects
from forms import ObjectsForm

# Create your views here.
def home(request):
	return render(request, 'index.html')

def upload(request):
	if request.method  == "POST":
		form = ObjectsForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/preview')
		else:
			print form.errors
	else:
		form = ObjectsForm()
	return render(request, 'upload.html', {'obj_form': form})

@csrf_exempt
def preview(request):
	obj_file = Objects.objects.all()
	a = obj_file[::-1]
	last_one = a[0]

	if request.method == "POST":
		whole_data = request.POST.get('whole_data')
		print whole_data

		last_one.coordinates = whole_data
		last_one.save()
		# print last_one.coordinates
		return HttpResponseRedirect('/gallery')
	return render(request, 'preview.html', {'last_one': last_one})

def gallery_single(request, id=1):
	# obj_file = [dict(id=i.id,title=i.title, obj_file=i.obj_file, coordinates=i.coordinates) for i in Objects.objects.filter(id=id)]
	obj_file = Objects.objects.get(id=id)
	return render(request, 'gallery_single.html', {'obj_one': obj_file})

def gallery(request):
	obj_file = Objects.objects.all()
	return render(request, 'gallery.html', {"obj_file": obj_file})
