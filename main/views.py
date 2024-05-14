from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'title': 'Home - Main',
        'content': "Furniture Store HOME",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': "Home - About us",
        'content': "About Us",
        'text_on_page': "Our store is one of the best in the country."
    }
    return render(request, 'main/about.html', context)

