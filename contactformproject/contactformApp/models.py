from django.db import models


class EmpData(models.Model):
    ename=models.CharField(max_length=100)
    sal=models.IntegerField()
    email=models.EmailField(max_length=100)
    loc=models.CharField(max_length=100)
    
