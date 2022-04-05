from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home_page(request):
    contex = {
        'posts':Post.objects.all(),
    }
    return render(request, 'blog/home.html', contex)


def about_page(request):
    contex = {
        'title':'About Page'
    }
    return render(request, 'blog/about.html', contex)
