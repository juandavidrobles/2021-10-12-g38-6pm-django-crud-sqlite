from django.db import models

class Customer(models.Model):
  name = models.CharField(max_length=50)
  address = models.CharField(max_length=50)
  email = models.EmailField(max_length=50)
  phone = models.CharField(max_length=15)

class Article(models.Model):
  name = models.CharField(max_length=50)
  category = models.CharField(max_length=50)
  price = models.IntegerField()

class Order(models.Model):
  number = models.IntegerField()
  date = models.DateField()
  delivered = models.BooleanField()
