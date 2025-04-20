from django.contrib.auth import forms
from .models import CustomUser

class CustomUserCreationForm(forms.UserCreationForm):
    # Specify the user model created while creating the user on admin page
    class Meta:
        model = CustomUser
        fields = [
            "email",
            "first_name", 
            "last_name",
            "role"
        ]
class CustomUserChangeForm(forms.UserChangeForm):
    # Specify the user model edited while editing on admin page
    class Meta:
        model = CustomUser
        fields = [
            "email",
            "first_name", 
            "last_name",
            "role"
        ]