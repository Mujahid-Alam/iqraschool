from django.contrib import admin
from django.urls import path
# APP
from studyApp.views import *

# Static Files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('courses/', courses, name='courses'),
    path('about/', about, name='about'),
    path('login/', loginpage, name='login'),
    path('logout/', logoutpage, name='logout'),
    path('team/', team, name='team'),
    path('ourStudent/', ourStudent, name='ourStudent'),
    path('coursesCategories/', coursesCategories, name='coursesCategories'),
    path('applyForAdmission/', applyForAdmission, name='applyForAdmission'),

    path('account/profile/', profile, name='account/profile'),
    path('account/profile/edit/', edit_profile, name='account/edit_profile'),
    path('account/my_courses/', my_courses, name='account/my_courses'),

    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)