import coreapi
import coreschema
from rest_framework import schemas
from rest_framework.schemas import ManualSchema
from rest_framework.schemas.openapi import AutoSchema
from drf_yasg import openapi


resend_otp_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    responses={200: 'OK'},
    properties={
        'mobile': openapi.Schema(type=openapi.TYPE_STRING),
    }
)

login_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    responses={200: 'OK'},
    properties={
        'mobile': openapi.Schema(type=openapi.TYPE_STRING),
        'password': openapi.Schema(type=openapi.TYPE_STRING),
    }
)


change_password_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    responses={200: 'OK'},
    properties={
        'mobile': openapi.Schema(type=openapi.TYPE_STRING),
        'password': openapi.Schema(type=openapi.TYPE_STRING),
        'confirm_password': openapi.Schema(type=openapi.TYPE_STRING),
    }
)


otp_verification_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    responses={200: 'OK'},
    properties={
        'mobile': openapi.Schema(type=openapi.TYPE_STRING),
        'otp': openapi.Schema(type=openapi.TYPE_STRING),
    }
)
