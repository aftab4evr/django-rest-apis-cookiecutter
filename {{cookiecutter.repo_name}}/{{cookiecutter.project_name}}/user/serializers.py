from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from .models import MyUser


class MyUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MyUser
        exclude = ('is_otp_verify',
                   'is_superuser', 'is_staff',
                   'last_login', 'is_active',)
