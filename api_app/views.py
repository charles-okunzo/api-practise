from django.shortcuts import render
from .request import get_data

# Create your views here.


def home(request):
    data = get_data()
    context = {
        'data': data
    }
    return render(request, 'index.html', context)