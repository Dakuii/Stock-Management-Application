from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm, CustomAuthenticationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Un compte a été créé pour {username}. Continuer à vous connecter.')
            return redirect('utilisateur-login')
    else:
        form = CreateUserForm()

    context = {
        'form': form,
    }
    return render(request, 'user/register.html', context)

def custom_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('tableau_de_bord-index')  # Rediriger vers la page de profil ou une autre page après la connexion
            else:
                # You can choose not to show any error message here
                pass
        else:
            # You can choose not to show any error message here
            pass
    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'user/login.html', context)
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Vous êtes connecté en tant que {username}.')
                return redirect('utilisateur-profile')  # Rediriger vers la page de profil ou une autre page après la connexion
            else:
                messages.error(request, form.error_messages['invalid_login'])
        else:
            messages.error(request, form.error_messages['invalid_login'])
    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'user/login.html', context)


def profile(request):
    return render(request, 'user/profile.html')

def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('utilisateur-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'user/profile_update.html', context)
