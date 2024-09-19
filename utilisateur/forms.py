from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext as _
from .models import Profile

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Nom d\'utilisateur')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    error_messages = {
        'invalid_login': "Nom d'utilisateur ou mot de passe incorrect. Veuillez réessayer.",
        'inactive': "Ce compte est inactif.",
    }

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label="Mot de passe*", 
                                widget=forms.PasswordInput,
                                help_text="Votre mot de passe ne peut pas être trop similaire à vos autres informations personnelles, doit contenir au moins 8 caractères, ne peut pas être un mot de passe couramment utilisé et ne peut pas être entièrement numérique.",
                                error_messages={
                                    'password_too_similar': _("Votre mot de passe ne peut pas être trop similaire à vos autres informations personnelles."),
                                    'min_length': _("Votre mot de passe doit contenir au moins 8 caractères."),
                                    'common_password': _("Votre mot de passe ne peut pas être un mot de passe couramment utilisé."),
                                    'numeric_password': _("Votre mot de passe ne peut pas être entièrement numérique."),
                                })
    password2 = forms.CharField(label="Confirmation du mot de passe*", 
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'Nom d\'utilisateur',
            'password1': 'Mot de passe',
            'password2': 'Confirmer le mot de passe',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = '150 caractères maximum. Lettres, chiffres et @/./+/-/_ uniquement.'


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        labels = {
            'username': 'Nom d\'utilisateur',
            'email': 'Email',
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('address', 'phone', 'image')
        labels = {
            'address': 'Adresse',
            'phone': 'Téléphone',
            'image': 'Image',
        }
