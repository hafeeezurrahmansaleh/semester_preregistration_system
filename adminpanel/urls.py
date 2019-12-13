from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.login,name='login'),
    path('index',views.index,name='index'),
    path('insert',views.insert,name='insert'),
    path('teacherDelete/<tid>/',views.teacherDelete,name='delete' ),
    path('studentDelete/<stid>/',views.studentDelete,name='stdelete' ),
    path('courseDelete/<courseCode>/',views.courseDelete,name='ctdelete' ),
]