from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Blog_Category(models.Model):
    blog_cat= models.CharField(max_length=30,unique=True) #field  primary key
    blogcat_img = models.ImageField(upload_to='images/') # field for images
    blogcat_description = models.CharField(max_length=300) # field for writing Description 
    def __str__(self):
        return self.blog_cat # save with name 

class Contact_Info(models.Model):
    u_email=models.EmailField()
    u_message=models.CharField(max_length=200)  
    def __str__(self):
        return self.u_email # it is used to save the data using email in data base

class Subscribe(models.Model):
    use_email=models.EmailField(unique=True)
    def __str__(self):
        return self.use_email

class Blog_Post(models.Model):
    blog_name=models.CharField(max_length=30)
    blog_img=models.ImageField(upload_to='images/')
    like_btn=models.IntegerField(default=0,null=True)
    view_btn=models.IntegerField(default=0,null=True)
    blog_description=RichTextField()
    blog_cat=models.ForeignKey(Blog_Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.blog_name)
  
class Blog_comments(models.Model):
    blog_author=models.ForeignKey(User,on_delete=models.CASCADE)
    blog_comment=models.CharField(max_length=1000)
    comment_date= models.DateTimeField(default=timezone.now)
    blog_idd=models.ForeignKey(Blog_Post,on_delete=models.CASCADE,related_name='comments')
    
    def __str__(self):
        return str(self.blog_author)

