from django.shortcuts import render , get_object_or_404
from .models import post
# Create your views here.
def home(request):
    context = 
    {
        'title' = 'الصفحة الرئيسية',
        'posts' = post.objects.all()
    }
    return render(request,'blog/index.html', context)

def about(request):
    return render(request,'blog/about.html' , {'title' : 'من انا'})

def post_detail(request , post_id):
    post = get_object_or_404(post,pk=post_id)
    context = {
        'title'  =  post,
        'post' = post,
    }
    return render(request,'blog/detail.html',context)