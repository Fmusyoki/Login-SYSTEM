from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login
from.models import User
from django.contrib.auth import logout as django_logout
from .models import User

# Create your views here.


# Register
def register(request):
    msg = None
    success = False

    

    if request.method == "POST":
        Username = request.POST['user']
        Email = request.POST['mail']
        ConfirmPassword =request.POST['pass1']
        Password = request.POST['pass2']
        
        new_user = User(Username=Username, Email=Email, ConfirmPassword=ConfirmPassword, Password=Password)
        new_user.save()
        
        
         
    return render(request, "authentication/register.html")

# Login
def login_page(request):
    if request.method =='POST':
        name = request.POST.get('username')
        passwd = request.POST.get('password')
        
        user = authenticate(request, username=name, password=passwd)
        
        if user is not None:
            django_login(request, user)
            return redirect('register')
        else:
            messages.success(request, 'Loggedin successfully.')
            return render(request, "authentication/home.html") 
            
          
    
    
    return render(request, "authentication/login.html") 
    # if request.method=='POST':
    #     Username = request.POST['me']
    #     Password = request.POST['pass1']
    #     user = authenticate(me=Username, pass1=Password)
    #     if user is not None:
    #         django_login(request,user)
    #         return render (request,'authentication/home.html')
    #     else:
    #         messages.error(request, "bad username")
    #         return render (request,'authentication/login.html')
    # return render (request,'authentication/login.html')

        
    # form = LoginForm(request.POST or None)
    # if request.method=='POST':
    #     Email = request.POST['mail']
    #     Password = request.POST['pass2']
    #     if form.is_valid():
    #         user=authenticate(request,Email=Email,Password=Password)
    #         if user is not None:
    #             django_login(request, user)
    #             return redirect('home')
    #         else:
    #             return HttpResponse ("Username or Password is incorrect!!!")
        
        

    # return render (request,'authentication/login.html')
    # form = LoginForm(request.POST or None)

    # msg = None

    # if not request.user.is_authenticated:
    #     if request.method == "POST":

    #         if form.is_valid():
    #             user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
    #             if user is not None:
    #                 login(request, user)
    #                 return redirect('home')
    #             else:
    #                 messages.error(request, 'Invalid credentials.')
    #         else:
    #             messages.error(request, 'Error validating the form.')
    #     return render(request, "authentication/login.html", {"form": form, "msg": msg})
    # return redirect("home")
    
    


    

# Dashboard
def home(request):
    if request.user.is_authenticated:
            
            return render(request, "authentication/home.html")
    return redirect('login')


def logout(request):
    django_logout(request)
    return redirect('login')