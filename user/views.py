from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib  import messages 
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'successful register {username}')
            return redirect('home')
    else:
        form = UserCreationForm()

    context = {
        'title' : 'التسجيل',
        'form' :  form,
    }
    return render(request,'user/register.html',context)