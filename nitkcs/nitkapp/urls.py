from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
path('',views.index,name='homeurl'),
path('faculty/',views.faculty,name='facultyurl'),
path('placements/',views.placements,name='placementurl'),
path('research/',views.research,name='researchurl'),
path('course/',views.coursesview,name='coursesurl'),

#<str:opti>

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
