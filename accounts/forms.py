from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')
    photo = forms.ImageField(required=False, help_text='Upload your profile photo (optional)')
    phone_number = forms.CharField(max_length=15, required=False, help_text='Your contact number (optional)')
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False, help_text='Your address (optional)')
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "photo", "phone_number", "address")
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            # Create or update user profile
            profile, created = UserProfile.objects.get_or_create(user=user)
            profile.photo = self.cleaned_data.get("photo")
            profile.phone_number = self.cleaned_data.get("phone_number")
            profile.address = self.cleaned_data.get("address")
            profile.save()
        return user

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Current Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your current password'
        })
    )
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your new password'
        })
    )
    new_password2 = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your new password'
        })
    )

