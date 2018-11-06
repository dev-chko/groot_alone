from django.db import models

# Create your models here.

class Signup(models.Model):
    id = models.CharField(max_length=10,primary_key=True)
    pw = models.CharField(max_length=15)
    name = models.CharField(max_length=5)
    e_mail = models.CharField(max_length=20)

class Notice(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    c_date = models.DateTimeField()