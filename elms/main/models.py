from django.db import models

# Teacher Model
class Teacher(models.Model):
    full_name = models.CharField(max_length=50)
    school_name = models.CharField(max_length=50)
    title = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

# Course Category Model
class CourseCategory(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        verbose_name_plural="Course Categories"

# Course Model
class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()

# Student Model
class Student(models.Model):
    full_name = models.CharField(max_length=50)
    school_name = models.CharField(max_length=50)
    grade = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    interests = models.TextField()