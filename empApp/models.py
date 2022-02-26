from django.db import models


# Create your models here.
class Employee(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    salary = models.FloatField()
    email = models.CharField(max_length=50)


class Programmer(models.Model):
    name = models.CharField(max_length=30)
    sal = models.FloatField()


class Project(models.Model):
    name = models.CharField(max_length=50)
    programmers = models.ManyToManyField(Programmer)
