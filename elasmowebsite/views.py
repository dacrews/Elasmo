from django.shortcuts import render
from .models import PorbBlue
from .models import Zambezi
from .models import BlueShark
import wikipediaapi

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def science(request):
    return render(request, 'science.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def data(request):
    porbblue = PorbBlue.objects.all()
    zambezi = Zambezi.objects.all()
    blueshark = BlueShark.objects.all()
    return render(request, 'data.html', {'porbblue': porbblue, 'zambezi': zambezi, 'blueshark': blueshark})

def sharks(request):
    shark_list = [
        'Nurse Shark',
        'Whitetip Reef Shark',
        'Sandbar Shark',
        'Blacktip Reef Shark',
        'Galapagos Shark',
        'Whale Shark',
        'Great White Shark',
        'Thresher Shark',
        'Blue Shark',
        'Oceanic Whitetip Shark',
    ]

    wiki = wikipediaapi.Wikipedia(
        'en',
        extract_format = wikipediaapi.ExtractFormat.WIKI
    )

    data = []
    key = 0

    for shark in shark_list:
        page = wiki.page(shark)
        title = page.title
        content = page.summary
        result = {key: {'title': title, 'content': content}}
        key += 1

        data.append(result)

    return render(request, 'sharks.html', {'data': data})

def resources(request):
    return render(request, 'resources.html', {})