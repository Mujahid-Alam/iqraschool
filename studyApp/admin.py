from django.contrib import admin

from .models import AdmissionForm, Courses, Instructors, OurStudents, CoursesCategories
# Register your models here.
class AdminAdmissionForm(admin.ModelAdmin):
    list_display = ['name', 'mother_name', 'father_name','contact', 'email', 'education','dob', 'gender', 'address']
class AdminCourses(admin.ModelAdmin):
    list_display = ['course_name', 'educator', 'hours','total_student', 'fees', 'img']
class AdminInstructors(admin.ModelAdmin):
    list_display = ['name', 'designation', 'facebook','twitter', 'instagram', 'image']
class AdminOurStudents(admin.ModelAdmin):
    list_display = ['name', 'profession', 'description', 'image']
class AdminCoursesCategories(admin.ModelAdmin):
    list_display = ['course_name', 'total_course', 'image']

admin.site.register(AdmissionForm, AdminAdmissionForm)
admin.site.register(Courses, AdminCourses)
admin.site.register(Instructors, AdminInstructors)
admin.site.register(OurStudents, AdminOurStudents)
admin.site.register(CoursesCategories, AdminCoursesCategories)



