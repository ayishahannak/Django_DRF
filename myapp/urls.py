from django.urls import path

from myapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('students_list', views.snippet_list, name='student_list'),
    path("student_detail/<int:pk>/",views.snippet_detail,name='student_detail'),
]