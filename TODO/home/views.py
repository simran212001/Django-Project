from django.http.response import HttpResponse
from django.shortcuts import render

from home.models import Task

# Create your views here.
def index(request):
    context = {'success' :False}
    # return HttpResponse('this is index for TODO')
    if request.method == 'POST':
        # print('this is post')
        task_title = request.POST['task_title']
        task_desc = request.POST['task_desc']
        print(task_title,task_desc)

        # To store the data in database table create instance
        ins = Task(task_title = task_title ,task_desc = task_desc)
        ins.save()

        context = {'success' :True}
    return render(request ,'index.html',context)

def task(request):
    AllTasks = Task.objects.all()
    # for item in AllTasks:
    #     print(item.task_title)
    context = {'tasks' : AllTasks}
    return render(request , 'task.html',context)