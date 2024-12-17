from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Textura - Главная',
        'content': 'Магазин тканей Textura'
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Textura - О нас',
        'content': 'О нас',
        'text_on_page': "Добро пожаловать в Textura — интернет-магазин, где качество встречается с вдохновением! Мы предлагаем широкий ассортимент тканей для шитья и творчества, чтобы каждая ваша идея стала реальностью."
    }
    return render(request, 'main/about.html', context)
