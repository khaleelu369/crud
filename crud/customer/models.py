from django.db import models

# Create your models here.
class position(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

class employee(models.Model):
    fullname=models.CharField(max_length=100) 
    emp_code=models.CharField(max_length=3)
    mobile=models.CharField(max_length=50)
    position=models.ForeignKey(position,on_delete=models.CASCADE) 

    def __str__(self):
        return self.fullname

    