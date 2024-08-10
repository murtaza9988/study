from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contact(request):
    return render(request,'contact.html')
def staff(request):
    return render(request,'staff.html')
def userform(request):
    return render(request,'userform.html',)

    finallysa=0
    data={}
    if request.method == 'POST':
        n1 = int(request.POST.get('num1'))
        n2 = int(request.POST.get('num2'))
        finallysa=n1+n2
        print(finallysa),
        data={
            'n1':n1,
            'n2':n2,
            'output':finallysa
             
        }

# def  couses(request):
#     return HttpResponse("welcome to my compute couses")
# def cousesdata(request ,cousesid):
#     return HttpResponse(cousesid)
