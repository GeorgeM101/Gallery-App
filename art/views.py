from unicodedata import category
from django.shortcuts import render
from django.http import Http404
from .models import Location, Category, Image
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):
    try:
        images = Image.objects.all()
        category = Category.objects.all()
        location = Location.objects.all()
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'index.html', {'images': images,'category': category, 'location':location})
