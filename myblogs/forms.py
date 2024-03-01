from .models import Blog_Category,Blog_Post,Blog_comments
from django.forms import ModelForm

 
class Blog_Form(ModelForm):
# specify the name of model to use
    class Meta:
         model = Blog_Category
# fields attribute to the special value '__all__' to indicate that all fields in the model should be used
         fields = "__all__" 
#if we want to exclude attribute of the ModelForm’s inner Meta class to a list of fields to be excluded from the form.
#exclude = ["title"]

class BlogPost_Form(ModelForm):
    class Meta:
        model =Blog_Post
        exclude=["like_btn","view_btn"]

class BlogComment_Form(ModelForm):
    class Meta:
        model=Blog_comments
        fields=["blog_comment"]