from django import forms
from .models import Comment , post


class NewComment(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name','email','body')


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(label='عنوان التدوينة')
    content = forms.CharField(label='نص التدوينة', widget=forms.Textarea)

    class Meta:
        model = post
        fields = ['title', 'content']