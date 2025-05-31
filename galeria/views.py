from django.shortcuts import render

def index(response):
    return render(response, 'galeria/index.html')

def imagem(response):
    return render(response, 'galeria/imagem.html')





