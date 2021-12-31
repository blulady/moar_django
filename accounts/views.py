from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login')
    context = {"form": form}
    return render(request, 'accounts/register.html', context)

def login_view(request):#using django authenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)#the form has request as an argument
        if form.is_valid():
            user = form.get_user() #this method is specific to AuthenticationForm
            login(request, user)
            return redirect('/') #'/' sends it to the homepage
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)

def login_viewold(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        #print(username, password) printing this is a safety issue
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Invalid username or password"}
            return render(request, "accounts/login.html", context)
        login(request, user)
        return redirect('/') #'/' sends it to the homepage
    return render(request, "accounts/login.html", {})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("/login/")
    return render(request, "accounts/logout.html", {})
