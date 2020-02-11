from django.shortcuts import render, get_object_or_404
from .models import post, Comment
from .forms import NewComment, PostCreateForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
def home(request):
    context = { 
        'title': 'الصفحة الرئيسية',
        'posts': post.objects.all(),
    }
    return render(request,'blog/index.html', context)

def about(request):
    return render(request,'blog/about.html' , {'title' : 'من انا'})

def post_detail(request , post_id):
    post = get_object_or_404(post,pk=post_id)
    comments = post.comment.filter(active = True)


    if request.method == 'POST':
        comment_form = NewComment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = NewComment()
    else:
        comment_form = NewComment()  

        
           
    context = {
        'title'  :  post,
        'post' : post,
        'comments' : comments,
        'comment_form' : comment_form,
    }
       
    return render(request,'blog/detail.html',context)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = post
    # fields = ['title', 'content']
    template_name = 'blog/new_post.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = post
    template_name = 'blog/post_update.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    