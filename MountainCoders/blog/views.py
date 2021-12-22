from django.http.response import HttpResponse
from django.shortcuts import render 

from blog.models import Blog

# Create your views here.
def home(request):
    return render(request,'home.html')

def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request,'blog.html',context)

def blogpost(request,slag):
    return HttpResponse(f'You are viewing {slag}')

def search(request):
    return render(request,'search.html')


def contact(request):
    return render(request,'contact.html')
