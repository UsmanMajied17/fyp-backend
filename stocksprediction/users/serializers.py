from rest_framework import serializers
# from django.contrib.auth.models import User
from users.models import User
from rest_framework.exceptions import ValidationError

# class AuthUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'username', 'password', 'password2']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'phone',
                  'is_admin']

    def save(self, **kwargs):
        userprofile = User(
            username=self.validated_data.get('username'),
            email=self.validated_data.get('email'),
            first_name=self.validated_data.get('first_name'),
            last_name=self.validated_data.get('last_name'),
            phone=self.validated_data.get('phone'),
            is_admin=self.validated_data.get('is_admin'),
        )

        password = self.validated_data['password']

        userprofile.set_password(password)
        userprofile.save()
        return userprofile