from django.shortcuts import redirect, render
from .models import Category, Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms





def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in successfully.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")

    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')

# adjust based on your project structure

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']  

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "You have registered successfully.")
                return redirect('home')
            else:
                messages.error(request, "Authentication failed after registration.")
                return redirect('register')
        else:
            messages.error(request, "Whoops! There was a problem with registration. Please try again.")
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})
    

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})

def category(request, foo):
    # replace Hyphens with Spaces
    foo = foo.replace('-', ' ')
    # Grab the Category from the URL
    try:
         category = Category.objects.get(name=foo)
         products = Product.objects.filter(category=category)
         return render(request, 'category.html', {'category': category, 'products': products})
    except:
        messages.error(request, "Category not found.")
        return redirect('home')

