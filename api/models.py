from django.db import models

# Creating company models here.

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT','IT'),('Non IT', 'Non IT'),('Mobile Phone', 'Mobile Phone')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)