from django.db import models
#template model view urls
from django.urls import reverse # new
# Create your models here.
class Post(models.Model):#import class models then creating subclas models.Model as Post
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        )
    body = models.TextField()
    def __str__(self):
        return self.title
        
    def get_absolute_url(self): # new
        return reverse('post_detail', args=[str(self.id)])
