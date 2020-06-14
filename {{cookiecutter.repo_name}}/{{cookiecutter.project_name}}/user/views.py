
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth import login, logout, authenticate

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from user.models import MyUser
from user.schema import (
    resend_otp_body, otp_verification_body, change_password_body, login_body
)
from user.serializers import(LoginSerializer,SignUpUserSerializer)




class SignUpView(generics.CreateAPIView):

    queryset = MyUser.objects.all()
    serializer_class = SignUpUserSerializer

    def create(self, request, *args, **kwargs):
        try:
            MyUser.objects.get(
                mobile=request.data['mobile'], is_otp_verify=True)
            return Response({'response_message': "Mobile no already exist.", }, status=status.HTTP_400_BAD_REQUEST)
        except MyUser.DoesNotExist:
            MyUser.objects.filter(mobile=request.data['mobile']).delete()

        try:
            MyUser.objects.get(
                email=request.data['email'], is_otp_verify=True)
            return Response({'response_message': "Email id already exist.", }, status=status.HTTP_400_BAD_REQUEST)
        except MyUser.DoesNotExist:
            MyUser.objects.filter(email=request.data['email']).delete()

        instance = super(SignUpView, self).create(request, *args, **kwargs)
        return Response({'response_message': "Signup successfully", 'data': instance.data}, status=status.HTTP_200_OK)



class ResentOTPView(APIView):
    @swagger_auto_schema(request_body=resend_otp_body, operation_description="Resent OTP")
    def post(self, request):
        params = request.data
        try:
            user = MyUser.objects.get(mobile=params['mobile'])
            user.otp_creation()
            user.sent_otp()
            return Response({'response_message': "OTP verify successfully"}, status=status.HTTP_200_OK)
        except MyUser.DoesNotExist:
            return Response({'response_message': "This mobile no is not associated with {{cookiecutter.project_name}}"}, 
            status=status.HTTP_400_BAD_REQUEST)


class OTPVerificationView(APIView):
    @swagger_auto_schema(request_body=otp_verification_body, operation_description="Resent OTP")
    def post(self, request):
        params = request.data
        try:
            user = MyUser.objects.get(mobile=params['mobile'])
            # if user.otp == params['otp']:
            if params['otp']:
                user.is_user_verified = True
                user.save()
                return Response({'response_message': "OTP verify successfully"}, 
                status=status.HTTP_200_OK)
            return Response({'response_message': "Otp miss-match please try again"}, 
            status=status.HTTP_400_BAD_REQUEST)
        except MyUser.DoesNotExist:
            return Response({'response_message': "This mobile no is not associated with {{cookiecutter.project_name}}"}, 
            status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    @swagger_auto_schema(request_body=change_password_body, operation_description="Change Password")
    def post(self, request):
        params = request.data
        try:
            user = MyUser.objects.get(mobile=params['mobile'])
            if params['password'] == params['confirm_password']:
                user.set_password(params['password'])
                user.save()
                return Response({'response_message': "Password changed successfully."}, 
                status=status.HTTP_200_OK)
            return Response({'response_message': "Password and confirm password does't match."}, 
            status=status.HTTP_400_BAD_REQUEST)
        except MyUser.DoesNotExist:
            return Response({'response_message': "This mobile no is not associated with {{cookiecutter.project_name}}"},
            status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    @swagger_auto_schema(request_body=login_body, operation_description="Login")
    def post(self, request):
        params = request.data
        try:
            user = MyUser.objects.get(mobile=params['mobile'])
            if user.is_user_verified:
                if user.check_password(params['password']):
                    login(request, user)
                    serializer = LoginSerializer(user)
                    return Response({"response_message": "Login Successfully", 
                    "data": serializer.data, "token": user.create_jwt()}, 
                    status=status.HTTP_200_OK)
                return Response({'response_message': "Please enter valid password."}, 
                status=status.HTTP_400_BAD_REQUEST)
            user.otp_creation()
            user.sent_otp()
            return Response({'response_message':  "Please verify your otp first"}, 
            status=status.HTTP_400_BAD_REQUEST)
        except MyUser.DoesNotExist:
            return Response({'response_message': "This mobile no is not associated with {{cookiecutter.project_name}}"}, 
            status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        return Response({"response_message": "Logout Successfully"
        }, status=status.HTTP_200_OK)
