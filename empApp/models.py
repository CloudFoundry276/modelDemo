from django.db import models


# Create your models here.
class Employee(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    salary = models.FloatField()
    email = models.CharField(max_length=50)


# Implemented Many To Many ORM
class Programmer(models.Model):
    name = models.CharField(max_length=30)
    sal = models.FloatField()


# Implemented Many To Many ORM
class Project(models.Model):
    name = models.CharField(max_length=50)
    programmers = models.ManyToManyField(Programmer)


# Implemented Many To One ORM
class Customer(models.Model):
    name = models.CharField(max_length=30)


# Implemented Many To One ORM
class PhoneNumber(models.Model):
    type = models.CharField(max_length=10)
    number = models.CharField(max_length=10)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
