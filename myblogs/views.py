from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog_Category,Contact_Info,Subscribe,Blog_Post,Blog_comments
from .forms import Blog_Form,BlogPost_Form,BlogComment_Form
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    # return HttpResponse('<h1>this is home page</h1>')
    #fetch data from db
    x=Blog_Category.objects.all() #take all objects and asign it to x we have created 3 thing food,adventure and travel in admin page
    # print(x)
    return render(request,'myblogs/home.html',{"category":x})#send context from backend to frontend

def contact(request):
    # return HttpResponse('<h1>this is contact page</h1>')
    if(request.method=='GET'):
        return render(request,'myblogs/contact.html')
    elif(request.method=='POST'):
        # user_email is the name of the email in contactpage
        email=request.POST.get('user_Email')
        message=request.POST.get('message')
        # u_email is model name and email is name of the variable 
        x=Contact_Info(u_email=email,u_message=message)
        # save data in db
        # X is haveing email address 
        x.save()
        return render(request,'myblogs/contact.html',{'feedback':'Your FeedBack is recieved ..We will work on it'})
    
@login_required(login_url='loginuser')
def subscribe(request):
    if(request.method=='GET'):
        return render(request,'myblogs/subscribe.html')
    elif(request.method=='POST'):
        mail=request.POST.get('user_Email')
        if(Subscribe.objects.filter(use_email=mail).exists()):
            return render(request,'myblogs/subscribe.html',{'feedback':'Already Subscribed'})
        else:
            x=Subscribe(use_email=mail)  #model.email= this views.email 
            x.save()
            return render(request,'myblogs/subscribe.html',{'feedback':'Thanks for Subscribing'})  
        
        # crispy form django
        # render in front end
        # ck editor proper text editor it is rich
        # confetti 
@login_required(login_url='loginuser')
def blog(request):
    x = BlogPost_Form() 
    # X will take whole modelform and convert it to html format 
    if request.method == "GET":
        return render(request,'myblogs/blog.html',{"x":x})
    else:
    # if you are constructing an object manually, you can assign the file object from request.FILES to the file field in the model,will only contain data if the request method was POST
        form = BlogPost_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home') 
        else:
            return render(request,'myblogs/blog.html',{"x":x})
 
   
def allblogs(request):
    list=Blog_Post.objects.all() 
    paginator = Paginator(list, 3)  # Show 3 blogs per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"myblogs/allblogs.html",{"page_obj":page_obj})

@login_required(login_url='loginuser')    
def blog_details(request,blog_id):
    # obj will get name of a particular id
    # queryset =Blog_Post.objects.filter(type='blog_name')
    # get_object_or_404(queryset)
    obj=get_object_or_404(Blog_Post,pk=blog_id)
    comment=BlogComment_Form()
    # fetch the likes count value
    x=obj.view_btn
    x+=1
    obj.view_btn=x
    obj.save()
    return render(request,'myblogs/blog_details.html',{"obj":obj,"comment":comment })

def loginuser(request):
    if request.method=='GET':
        return render(request,'myblogs/loginuser.html',{"form":AuthenticationForm()})
    else:
        name=request.POST.get('username')
        passw=request.POST.get('password')
        user=authenticate(request,username=name,password=passw)
        if(user is None):
            return render(request,'myblogs/loginuser.html',{'form':AuthenticationForm(),'error':'Invalid Credentials'})
        else:
            login(request,user)
            # it is the name of the function home
            return redirect('home')
    
def signupuser(request):
    if request.method=='GET':
        return render(request,'myblogs/signupuser.html',{"form":UserCreationForm()})
    else:
        a=request.POST.get("username")
        b=request.POST.get("password1")
        c=request.POST.get("password2")
        if(b==c):
            # username is unique
            if(User.objects.filter(username=a)):
               return render(request,'myblogs/signupuser.html',{"form":UserCreationForm(),"error":"User name already exists.Try again with differnt unique name"})
            else:
                user=User.objects.create_user(username=a,password=c) 
                user.save()
                login(request,user)
                return redirect('home')   
        else:
            # password mismatch
            return render(request,'myblogs/signupuser.html',{"form":UserCreationForm(),'error':'Password Missmatch.Try again'})
    
def logoutuser(request):
    if(request.method=="GET"):
        logout(request)
        return redirect('home')
    
   
def blog_display(request,blog_cat):
    x=Blog_Category.objects.get(blog_cat=blog_cat)
    # a will take all the query of blog in that particular category
    a=Blog_Post.objects.filter(blog_cat=x)
    paginator = Paginator(a, 3)  # Show 3 blogs per page.
    page_number = request.GET.get("page")
    object = paginator.get_page(page_number)
    return render(request,'myblogs/allblogs.html',{"page_obj":object})
 
def findproduct(request):
    if(request.method=="POST"):
        x=request.POST.get("search")
        fetchdata=Blog_Post.objects.filter(Q(blog_name__icontains =x))
        if fetchdata:
            return render(request,"myblogs/allblogs.html",{"page_obj":fetchdata})
        else:
            return render(request,"myblogs/allblogs.html",{"warning":"no Such product is found"})

@login_required(login_url='loginuser')     
def addlikes(request,blog_id):
    # fetch addlike
    obj=get_object_or_404(Blog_Post,pk=blog_id)
    x=obj.like_btn
    x+=1
    obj.like_btn=x
    obj.save()
    return redirect('blog_details',obj.id)

@login_required(login_url='loginuser')  
def blog_comment(request,blog_id):
    obj=get_object_or_404(Blog_Post,pk=blog_id)
    if request.method == "GET":
        return render(request,'myblogs/blog_details.html',{"obj":obj})
    else:
    # if you are constructing an object manually, you can assign the file object from request.FILES to the file field in the model,will only contain data if the request method was POST
        form = BlogComment_Form(request.POST)
        if form.is_valid(): 
            comment = form.save(commit=False)
            comment.blog_idd = obj
            comment.blog_author = request.user
            form.save()
            return redirect('blog_details',blog_id=obj.id)
        else:
            return render(request,'myblogs/allblogs.html',{"obj":obj})
   
@login_required(login_url='loginuser')      
def delete_comment(request,blog_id,comment_id):
    obj=get_object_or_404(Blog_comments,pk=comment_id)
    obj.delete()
    return redirect('blog_details',blog_id=blog_id)

@login_required(login_url='loginuser') 
def edit_comment(request, blog_id, comment_id):
    comment = get_object_or_404(Blog_comments, pk=comment_id)
    if request.method == 'POST':
        form = BlogComment_Form(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_idd = get_object_or_404(Blog_Post, pk=blog_id)
            comment.blog_author = request.user
            comment.save()
            return redirect('blog_details', blog_id=blog_id)
    else:
        form = BlogComment_Form(instance=comment)
        return render(request, 'myblogs/edit_comment.html', {'form': form})
    
    
        
        
    