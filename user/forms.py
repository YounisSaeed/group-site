from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=30), 
    email   = forms.EmailField(),
    first_name = forms.CharField(),
    last_name  = forms.CharField(),
    password = forms.CharField(label='Password',widget=forms.PasswordInput(),min_length=8),
    #password2 = forms.CharField(label='confirm Password',widget=forms.PasswordInput(),min_length=8),

    #class Meta:
    #    model = User
    #    fields = ('username' , 'email' , 'first_name' , 'last_name' , 'password1' , 'password2')
    class Meta:
        model = User
        fields = ('username' , 'email' , 'first_name' , 'last_name' , 'password')


    #confirm password
    #def clean_password2(self):
    #    cd = self.cleaned_data
    #    if cd['password1'] != cd['password2']:
    #        raise forms.ValidationError('password is not correct')
    #    return cd['password2']

    #username not in database with the same username (distinct)
    def clean_username(self):
        cu = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('username is used already')
        return cu['username']


class LoginForm(forms.ModelForm):
    username = forms.CharField(label='اسم المستخدم')
    password = forms.CharField(
        label='كلمة المرور', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='الاسم الأول')
    last_name = forms.CharField(label='الاسم الأخير')
    email = forms.EmailField(label='البريد الإلكتروني')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)