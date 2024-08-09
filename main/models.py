from django.db import models

class student(models.Model):
    First_name=models.CharField(max_length=30)
    Last_name=models.CharField(max_length=30)
    father_name=models.CharField(max_length=30)
    address=models.CharField(null=True,max_length=30)
    grade=models.CharField(null=True ,max_length=30)
    passind_year=models.DateField(null=True,blank=True)

    def __str__(self) :
        return f"{ self .First_name}"
    
     
     
     