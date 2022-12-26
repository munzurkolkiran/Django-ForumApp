from django import forms
from .models import CustomUserModel


class ProfileForm(forms.Form):
    class Meta:
        model = CustomUserModel
        fields = ['profile_pic', ]
        labels = {
            'profile_pic': 'Profile picture'
        }
