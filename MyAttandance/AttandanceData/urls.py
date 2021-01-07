from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
                  path('', views.index, name='index'),
                  path('student/', views.studentData, name='student'),
                  path('faculty/', views.facultyData, name='faculty'),
                  path('loginstudent/', views.loginstudent, name='loginstudent'),
                  path('loginfaculty/', views.loginfaculty, name='loginfaculty')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
