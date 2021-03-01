from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, 'webIqlimApp/home.html')

def tienda(request):

    return render(request, 'webIqlimApp/tienda.html')

def blog(request):

    return render(request, 'webIqlimApp/blog.html')

def contacto(request):

    return render(request, 'webIqlimApp/contacto.html')


