from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):

    #id = models.IntegerField(primary_key=True, blank=False)
    title = models.CharField(max_length=300)
    content = models.TextField()
    #author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
