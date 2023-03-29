from rest_framework import serializers
from .models import NewUser

class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = (
            "id",
            "username",
            "first_name",
            "is_admin",
            "is_superuser",
            "password",
        )