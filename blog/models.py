from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-post_date', )


class Comment(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    body = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    Post = models.ForeignKey(
        post, on_delete=models.CASCADE , related_name = 'comments')
    def __str__(self):
        return 'علق {} على {} .'.format(self.name,self.Post)
    class Meta:
        ordering = ('-comment_date', ) 
