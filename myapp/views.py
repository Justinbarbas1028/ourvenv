from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentRegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import Student

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.is_admin:
                        return redirect('admin_dashboard')  # Redirect admin users to admin dashboard
                    else:
                        return redirect('home')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'pages/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.set_password(form.cleaned_data['password'])
            student.save()
            return redirect('register')
    else:
        form = StudentRegistrationForm()
    return render(request, 'pages/register.html', {'form': form})

def index(request):
    return render(request, 'pages/index.html')

@login_required
def administrator_page(request):
    if not request.user.is_admin:
        return HttpResponse('Unauthorized', status=401)
    return render(request, 'pages/administrator_page.html')

@login_required
def home(request):
    return render(request, 'pages/homepage.html')

@login_required
def about(request):
    return render(request, 'pages/about.html')

@login_required
def courses(request):
    return render(request, 'pages/courses.html')

@login_required
def subjects(request):
    return render(request, 'pages/subjects.html')

@login_required
def grades(request):
    return render(request, 'pages/grades.html')

@login_required
def profile(request):
    return render(request, 'pages/profile.html')

@login_required
def admin_student_list(request):
    students = Student.objects.all()
    return render(request, 'pages/admin_student_list.html', {'students': students})

@login_required
def admin_dashboard(request):
    if not request.user.is_admin:
        return HttpResponse('Unauthorized', status=401)
    return render(request, 'pages/administrator_page.html')

@login_required
def student_dashboard(request):
    if request.user.is_admin:
        return HttpResponse('Unauthorized', status=401)
    return render(request, 'pages/home.html')


def user_logout(request):
    logout(request)
    return redirect('user_login')
