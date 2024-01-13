from django.db import models

# Teacher Model
class Teacher (models.Model):
    full_name=models.CharField(max_length=50)
    school_name=models.CharField(max_length=50)
    title=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    phone_no=models.CharField(max_length=20)
    address=models.TextField()

# Course Model
class Teacher (models.Model):
    full_name=models.CharField(max_length=50)
    school_name=models.CharField(max_length=50)
    title=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    phone_no=models.CharField(max_length=20)
    address=models.TextField()