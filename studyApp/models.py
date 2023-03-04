from django.db import models

# Create your models here.

# AdmissionForm
class AdmissionForm(models.Model):
    name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    contact = models.IntegerField()
    email = models.EmailField()
    education = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=200)
    address = models.TextField()
    
# Courses
class Courses(models.Model):
    course_name = models.CharField(max_length=200)
    educator = models.CharField(max_length=200)
    hours = models.CharField(max_length=200)
    total_student = models.CharField(max_length=200)
    fees = models.IntegerField()
    img = models.ImageField(upload_to='coursesImage')

# Instructors
class Instructors(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200, blank = True)
    twitter = models.CharField(max_length=200, blank = True)
    instagram = models.CharField(max_length=200, blank = True)
    image = models.ImageField(upload_to='instructorsImage', blank = True)

# Our Students
class OurStudents(models.Model):
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='StudentsImage', blank = True)

# Courses Categories
class CoursesCategories(models.Model):
    course_name = models.CharField(max_length=200)
    total_course = models.CharField(max_length=200)
    image = models.ImageField(upload_to='CoursesCategoriesImage', blank = True)

