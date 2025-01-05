from django .shortcuts import render,redirect 
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login as auth_login,logout,authenticate
from . models import todoo
def signup(request):
   if request.method=='POST':
      username=request.POST['username']
      email=request.POST['email']
      password=request.POST['password']
      if User.objects.filter(username=username).exists():
          messages.error(request, 'Username already exists.')
          return render(request, 'signup.html')
      User.objects.create_user(username,email,password).save()
      return redirect(reverse('login'))
   return render(request,'signup.html')

def login(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
         print("hai")
         auth_login(request,user)
         return redirect(reverse('todo_list'))
      else:
          print("hello")
          return redirect(reverse('login'))
   return render(request,'login.html')


def todo_list(request):
    todos = todoo.objects.all()  # Fetch all Todo items from the database
    return render(request, 'todo.html', {'todos': todos})  # Render the template with the Todo items