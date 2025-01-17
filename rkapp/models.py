from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Department(models.Model):
  name=models.CharField(max_length=50, null=False)
  location= models.CharField(max_length=50)

  def __str__(self):
    return self.name
class Role(models.Model) :
  name=models.CharField(max_length=100 , null=False)
  def __str__(self):
    return self.name
  
class Employee(models.Model):
  first_name= models.CharField(max_length=100, null=False)
  last_name= models.CharField(max_length=100)
  dept= models.ForeignKey(Department,on_delete=CASCADE)
  salary= models.IntegerField(default=0)
  bonus= models.IntegerField(default=0)
  role= models.ForeignKey(Role,on_delete=CASCADE)
  phone= models.IntegerField(default=0)
  hire_date= models.DateField(null=False)
  def __str__(self):
    return "%s %s %s" %(self.first_name,self.last_name,self.phone)
  

