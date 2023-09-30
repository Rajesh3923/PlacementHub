from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import  settings
from app.views import studentlogin,stureg,success,student_admin,register_admin,successadmin,admin_profile,adminlogin,student_dashboard,student_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', studentlogin, name='studentlogin'),
    path('studentlogin/', studentlogin, name='studentlogin'),
    path('studentlogin/stureg/',stureg, name='stureg'),
    path('success/',success, name='success'),
    path('successadmin/',successadmin, name='successadmin'),
    path('app/', include('app.urls')),
    path('student/', include('app.urls')),
    path('adminlogin/register_admin/',register_admin,name="register_admin"),
    path('student_admin/adminlogin/',adminlogin,name='adminlogin'),
    path('student_admin/',student_admin,name='student_admin'),
    path('student_admin/admin_profile/',admin_profile,name='admin_profile'),
    path('adminlogin/',adminlogin,name='adminlogin'),
    path('/',studentlogin,name='studentlogin'),
    path('studentlogin/student_dashboard',student_dashboard, name='student_dashboard'),
    path('student_dashboard',student_dashboard, name='student_dashboard'),
    path('student_profile',student_profile,name='student_profile'),
    path('register_admin/',register_admin,name='register_admin'),



    
    


]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)