from django.db import models


class Employee(models.Model):
    Emp_Name = models.CharField(max_length=255)
    Emp_Pwd = models.CharField(max_length=255)
    Emp_Email = models.CharField(max_length=255)
    Emp_Age = models.IntegerField()
    Emp_Designation = models.CharField(max_length=255)
    EmpAddress = models.CharField(max_length=255)


class Tbl_Inward(models.Model):
    Sender_Name = models.CharField(max_length=255)
    Sender_Letter_Number = models.IntegerField()
    Sender_Letter_Date = models.DateField(null=True)
    Sender_Letter_Subject = models.CharField(max_length=255)
    Sender_Letter_Type = models.CharField(max_length=255)
    Sender_Letter_Compliance_Date = models.DateField(null=True)
    Office_Letter_Number = models.IntegerField()
    Office_Letter_Date = models.DateField(null=True)
    Office_Letter_Marked_To = models.CharField(max_length=255)
    Officer_Remarks = models.CharField(max_length=255)
    Office_Compliance_Status = models.CharField(max_length=255)






