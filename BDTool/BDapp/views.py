from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def add_project(request):
           form1 = Client_Form(request.POST or None)
           if form1.is_valid():
               form1.save()

           form2 = Project_Form(request.POST or None)
           if form2.is_valid():
             client= Client.objects.get(skype_id=request.POST.get('skype_id'))
             pro=Project.objects.create(
                 project_name= request.POST.get('project_name'),
                 url_name = request.POST.get('url_name'),
                 domain_name=request.POST.get('domain_name'),
                 project_desrciption=request.POST.get('project_desrciption'),
                 attachment=request.POST.get('attachment'),
                 client=client,
             )
             list=request.POST.getlist('technology')
             for i in list:
                 tec=Technology.objects.get(pk=i)
                 pro.technology.add(tec)

           return render(request,'add_project.html',{'form1':form1,'form2':form2})



