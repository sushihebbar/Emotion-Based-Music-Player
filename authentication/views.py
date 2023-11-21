from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, RegistrationForm
from django.contrib import messages

# Create your views here.
def login_request(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    context = {
        'form': form,
        'title': title,
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"You are now logged in as {user}")
            return redirect('index')
        else:
            messages.error(request, 'Username or Password is incorrect!')
    else:
        # Display form errors if the form is invalid
        print(form.errors)
        messages.error(request, 'Invalid username or password.')

    return render(request, 'authentication/login.html', context=context)


def signup_request(request):
    title = "Create Account"
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    context = {'form': form, 'title': title}
    return render(request, 'authentication/signup.html', context=context)


def logout_request(request):
    logout(request)
    # messages.info(request, "Logged out successfully!")
    return redirect('index')
