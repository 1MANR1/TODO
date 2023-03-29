from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import NewUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = NewUser
        fields = UserCreationForm.Meta.fields + ("name",)


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = NewUser
        fields = fields = UserChangeForm.Meta.fields