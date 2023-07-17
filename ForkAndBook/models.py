from django.db import models

# Create your models here.

class Student(models.Model):
    StudID = models.CharField(max_length=11, primary_key=True)
    StudName = models.TextField(max_length=255)
    StudPhone = models.CharField(max_length=11)
    StudPass = models.CharField(max_length=10)
    
class Employee(models.Model):
    EmployeeID = models.CharField(max_length=11, primary_key= True)
    EmployeeName = models.TextField(max_length=255)
    EmployeePhone = models.CharField(max_length=11)
    EmployeePass = models.CharField(max_length=10)


class Menu(models.Model):
    MenuID = models.CharField(max_length=2, primary_key=True)
    MenuName = models.TextField(max_length=255)
    MenuPrice = models.IntegerField()
    EmployeeID = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)

class FoodBook(models.Model):
    StudID = models.ForeignKey(Student,on_delete=models.CASCADE, null=True)
    MenuID = models.ForeignKey(Menu,on_delete=models.CASCADE, null=True)
    EmployeeID = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    Quant = models.IntegerField(default=1)
    Status = models.CharField(max_length=128, default="Request Pending")
