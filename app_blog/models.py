from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=40, null=True)
    description = models.TextField(null=True) 

    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    name = models.CharField(max_length=40, null=True)
    parent_category = models.ForeignKey(to=Category, on_delete=models.CASCADE, null=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return f"{self.parent_category} : {self.name}"
    
class Post(models.Model):
    class Status(models.TextChoices):
        REJECTED = 'rejected'
        APPROVED = 'approved'
        PENDING = 'pending'

    title = models.CharField(max_length=100, null=True, unique=True)
    text = models.TextField(null=True)
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.PENDING)
    category = models.ForeignKey(to=SubCategory, on_delete=models.SET_NULL, null=True)
    
    def __repr__(self):
        return self.title
    
    def __str__(self):
        return f"{self.title} | {self.user}"

class PostImages(models.Model):
    file = models.FileField(null=True, upload_to='./posts')
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='files', null=True)

    def __str__(self):
        return f"{self.id} :: {self.post}"
    
class Comment(models.Model):
    text = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user} : {self.post}"