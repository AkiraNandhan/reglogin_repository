from django.shortcuts import render
from .forms import EmpForm
from .models import EmpData
from django.http.response import HttpResponse

def contact_view(request):
    if request.method=="POST":
        eform=EmpForm(request.POST)
        if eform.is_valid():
            ename1=request.POST.get('ename', '')
            sal1 = request.POST.get('sal', '')
            email1=request.POST.get('email', '')
            loc1 = request.POST.get('loc', '')

            data=EmpData(ename=ename1,  sal=sal1, email=email1, loc=loc1)

            data.save()
            eform=EmpForm()
            return render(request,'emp_home.html',{'eform':eform})
        else:
            return HttpResponse("plz enter all required fields...")
    else:
        eform=EmpForm()
        return render(request,'emp_home.html',{'eform':eform})






