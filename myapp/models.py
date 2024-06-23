# # models.py
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#
#
# class StudentManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('Students must have an email address')
#         email = self.normalize_email(email)
#         student = self.model(email=email, **extra_fields)
#         student.set_password(password)
#         student.save(using=self._db)
#         return student
#
#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_admin', True)
#         return self.create_user(email, password, **extra_fields)
#
#
# class Student(AbstractBaseUser):
#     email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     date_of_birth = models.DateField(null=True, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#
#     objects = StudentManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     def __str__(self):
#         return self.email
#
#     def has_perm(self, perm, obj=None):
#         return True
#
#     def has_module_perms(self, app_label):
#         return True
#
#     @property
#     def is_staff(self):
#         return self.is_admin

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class AccountManager(BaseUserManager):
    def create_user(self, student_number, password=None, **extra_fields):
        if not student_number:
            raise ValueError('Accounts must have a student number')
        user = self.model(student_number=student_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, student_number, password, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(student_number, password, **extra_fields)

class Account(AbstractBaseUser):
    student_number = models.CharField(max_length=20, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = AccountManager()

    USERNAME_FIELD = 'student_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.student_number

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return self.name

class Student(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    subjects = models.ManyToManyField(Subject, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Professor(models.Model):
    id_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    subjects = models.ManyToManyField(Subject, blank=True)

    def __str__(self):
        return f"Prof. {self.first_name} {self.last_name}"
