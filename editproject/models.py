from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=75)
    phone_no = models.IntegerField(default=170)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)


class Tasks(models.Model):
    task_ID = models.AutoField(primary_key=True)
    taskname = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    time_taken = models.CharField(max_length=50)

class Attendance(models.Model):
    AID = models.AutoField(primary_key=True)
    date = models.DateField()
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)

class IssueFaced(models.Model):
    issue_id = models.AutoField(primary_key=True)
    issue_discription = models.CharField(max_length=2000)
    task = models.ForeignKey(Tasks,on_delete=models.CASCADE)

class Skills(models.Model):
    skills_id = models.AutoField(primary_key=True)
    skills_list = models.CharField(max_length=100)

class Skills_Matrix(models.Model):
    sm_id = models.AutoField(primary_key=True)
    skills = models.ForeignKey(Skills,on_delete=models.CASCADE)
    Rating = models.CharField(max_length=25)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)

