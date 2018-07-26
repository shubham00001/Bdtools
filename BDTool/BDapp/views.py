from django.shortcuts import render
from .forms import *
# Create your views here.
def add_project(request):
           form1=Project_Form(request.POST or None)
           form2=Client_Form(request.POST or None)
           if form1.is_valid():
               form1.save()

           if form2.is_valid():

               form2.save()

           return render(request,'add_project.html',{'form1':form1,'form2':form2})
