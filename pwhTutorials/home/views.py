from django.shortcuts import render , HttpResponse

def home(request):
    return HttpResponse("This is home Views...which is created by home app..")

def paths(request):
    return HttpResponse("This is paths views..........created by home app")

def learning(request):
    return HttpResponse("This is for learning views.")