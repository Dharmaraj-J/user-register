from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .forms import StudentRegistration
from .models import User
def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(id=1,name=nm, email=em, password=pw)
            reg.save()
    else:
        fm = StudentRegistration()
    return render(request,'index.html',{'form':fm})