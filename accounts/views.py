from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from contacts.models import Contact

def register(request):
    if request.method == 'POST':
        # Registration Code Here
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        # Matching passwords
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exist')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exist')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                    user.save()
                    messages.success(request, 'Successfully Registered. Login Now!')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords not match!')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        # Login Code Here
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

@login_required
def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }

    return render(request, 'accounts/dashboard.html', context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out!')
        return redirect('login')