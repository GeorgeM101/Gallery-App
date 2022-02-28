from unicodedata import category
from django.shortcuts import render
from django.http import Http404
from .models import Location, Category, Image
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    try:
        images = Image.objects.all()
        category = Category.objects.all()
        location = Location.objects.all()
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'index.html', {'images': images,'category': category, 'location':location})


def search(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        searched_category = Image.search_by_category(search_term)
        print(searched_category)
        return render(request, 'search.html')
