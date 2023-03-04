from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as  auth_login
from django.contrib.auth import logout as  auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):
    course_data = Courses.objects.all()
    instructors_data = Instructors.objects.all()
    our_students_data = OurStudents.objects.all()
    courses_categories_data = CoursesCategories.objects.all()
    context = {
        'courses': course_data,
        'instructors': instructors_data,
        'our_students': our_students_data,
        'courses_categories': courses_categories_data,
    }
    return render(request, 'index.html', context)

# Course
def courses(request):
    mydata = Courses.objects.all()
    context = {
        'courses': mydata,
    }
    return render(request, 'courses.html', context)

# about 
def about(request):
    return render(request, 'about.html', {})

# coursesCategories 
def coursesCategories(request):
    courses_categories_data = CoursesCategories.objects.all()
    context = {
        'courses_categories': courses_categories_data,
    }
    return render(request, 'coursesCategories.html', context)

# LOGIN 
def loginpage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username = email, password = password)
        if user is not None:
            auth_login(request,user)
            return redirect('account/profile')
        else:
            return redirect('login')
    return render(request, 'login.html', {})

# LOGOUT 
def logoutpage(request):
    auth_logout(request)
    
    return render(request,'index.html')

#  Team 
def team(request):
    instructors_data = Instructors.objects.all()
    context = {
        'instructors': instructors_data,
    }
    return render(request, 'team.html', context)

# Our Student 
def ourStudent(request):
    our_students_data = OurStudents.objects.all()
    context = {
        'our_students': our_students_data,
    }
    return render(request, 'ourStudent.html', context)



# ApplyforAdmission
def applyForAdmission(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mother_name = request.POST.get('mother_name')
        father_name = request.POST.get('father_name')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        education = request.POST.get('education')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        student_user = User.objects.create_user(email, email, contact)
        student_user.save()

        a = AdmissionForm()
        a.name = name
        a.mother_name = mother_name
        a.father_name = father_name
        a.contact = contact
        a.email = email
        a.education = education
        a.dob = dob
        a.gender = gender
        a.address = address
        a.save()
        return redirect('login')

    return render(request, 'applyForAdmission.html',{})

# Profile 
@login_required(login_url='login')
def profile(request):
    user = request.user
    # print('------------user id---------', user.id)
    # print('------------user id---------', user.email)
    return render(request, 'account/profile.html', {'user': user})

@login_required(login_url='login')
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        # Update the user's profile fields with the submitted data
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        # messages.success(request, 'Your profile has been updated.')
        return redirect('account/profile')
    return render(request, 'account/edit_profile.html', {'user': user})

# my_courses 
def my_courses(request):
    return render(request, 'account/my_courses.html', {})
