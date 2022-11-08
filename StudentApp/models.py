from django.db import models


class Employee(models.Model):
    Emp_Name = models.CharField(max_length=255)
    Emp_Pwd = models.CharField(max_length=255)
    Emp_Email = models.CharField(max_length=255)
    Emp_Age = models.IntegerField()
    Emp_Designation = models.CharField(max_length=255)
    EmpAddress = models.CharField(max_length=255)
    class Emp:
        db_table = "Employees"



