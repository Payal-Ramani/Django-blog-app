from django.db import models
from datetime import datetime

class Authors(models.Model):
    name = models.CharField(max_length=100)
    about_author = models.TextField()

    def __str__(self):
        return self.name

class Blogs(models.Model):
    author = models.ForeignKey(Authors,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    posted_date = models.DateTimeField(default=datetime.now())
    content = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blogs,on_delete=models.CASCADE)
    comment_content = models.TextField()
    commented_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.comment_content