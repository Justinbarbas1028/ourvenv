# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('subjects/', views.subjects, name='subjects'),
    path('courses/', views.courses, name='courses'),
    path('grades/', views.grades, name='grades'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('administrator_page/', views.administrator_page, name='administrator_page'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_student_list/', views.admin_student_list, name='admin_student_list'),
]
