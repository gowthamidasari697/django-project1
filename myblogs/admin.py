from django.contrib import admin
from .models import Blog_Category
from .models import Contact_Info
from .models import Subscribe
from .models import Blog_Post,Blog_comments

# Register your models here. from models page when we are creating data base

admin.site.register(Blog_Category)
admin.site.register(Contact_Info)
admin.site.register(Subscribe)
admin.site.register(Blog_Post)
admin.site.register(Blog_comments)


