from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Student, Account

class StudentRegistrationForm(forms.ModelForm):
    student_number = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'sex', 'contact_number', 'email', 'course']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def save(self, commit=True):
        user = Account(
            student_number=self.cleaned_data['student_number'],
            is_active=True,
            is_admin=False
        )
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        student = super().save(commit=False)
        student.account = user
        if commit:
            student.save()
            self.save_m2m()
        return student

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Student Number")
    password = forms.CharField(widget=forms.PasswordInput)

#h