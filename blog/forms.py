from django import froms
from .models import Comment


class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        field = ('name','email','body')