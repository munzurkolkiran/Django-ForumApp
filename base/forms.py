from django.forms import ModelForm
from . models import Room
from django.contrib.auth.forms import UserCreationForm
from account.models import CustomUserModel


class RoomForm(ModelForm):
    class Meta:
        model = Room
     
        fields = ('host',
                    'topic',
                    'name',
                    'description',
        )

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'avatar',
        )
