from django.shortcuts import render
from.models import student
def student_data(request):

  studen=student.objects.all()
  context={
 'data':studen
  }
  return render(request,'data.html',context)



