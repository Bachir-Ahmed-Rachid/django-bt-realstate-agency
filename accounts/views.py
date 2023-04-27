from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contact.models import Contact  
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
             auth.login(request,user)
             messages.success(request, 'successfully logged in.')
             return redirect('dashboard')
        else:
            messages.error(request, 'wrong credentials.')
            return redirect('login')


    return render(request,'accounts/login.html')
def register(request):
     if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password != password2:
            messages.error(request, "password didn't match.")
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'This username is taken.')
            return redirect('register')
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'This email is been used.')
                return redirect('register')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password
        
                )
                auth.login(request,user)
                messages.success(request, 'successfully logged in.')
                return redirect('index')
     else:
        return render(request,'accounts/register.html')
    
def dashboard(request):
    user_contact=Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context={
        'user_contact':user_contact
    }
    return render(request,'accounts/dashboard.html',context)
    
def logout(request):
    if request.method=='POST':
        print('yoo')
        auth.logout(request)
        messages.success(request, 'successfully logged out.')
    return redirect('index')
    
    