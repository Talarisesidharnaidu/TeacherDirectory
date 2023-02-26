
from django.urls import path
from .views import  TeacherList,TeachersData

urlpatterns = [
    path('',TeacherList.as_view()),
    path('TeacherDetails/<int:pk>/',TeachersData.as_view()),
]
