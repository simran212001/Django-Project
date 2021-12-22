from django.http.response import HttpResponse
from django.shortcuts import render

from home.models import Contact

# Create your views here.
def home(request):
    # return HttpResponse("this is home page")
    context = {
        'name':'Simran' ,'course' :'Django'
    }
    return render(request , 'home.html',context)

def about(request):
    # return HttpResponse("this is about page")

    return render(request , "about.html")

def projects(request):
    # return HttpResponse("this is projects page")
    return render(request , 'projects.html')

def contact(request):
    # return HttpResponse("this is contact page")
    if request.method =='POST':
        print('this is post')
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        print(name,email,phone,desc)

        ins = Contact(name=name ,email=email,phone=phone,desc=desc)
        ins.save()

    return render(request , 'contact.html')   