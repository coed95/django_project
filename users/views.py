from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')

            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username is already taken.')
                return redirect('blog-register')
            else:
                form.save()
                messages.success(request, f'Account created for {username}.')
                return redirect('blog-home')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})