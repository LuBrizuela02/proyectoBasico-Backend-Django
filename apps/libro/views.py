from django.shortcuts import render
from .models import Libro

# Create your views here.
def lista_libros(request):
    return render(request, 'lista_libros.html', {})