from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from .models import MyUser


class SignUpUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        instance = MyUser.objects.create(**validated_data)
        instance.set_password(validated_data['password'])
        instance.save()
        instance.otp_creation()
        instance.sent_otp()
        return instance

    class Meta:
        model = MyUser
        fields = ("last_name", "first_name", "email", "mobile", "code")


class LoginSerializer(serializers.ModelSerializer):
    image = SerializerMethodField()

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None

    code = SerializerMethodField()

    def get_code(self, obj):
        if obj.code:
            return obj.code.code
        return None

    class Meta:
        model = MyUser
        fields = ("uuid", "image", "first_name",
                  "last_name", "email", "mobile", "code")
