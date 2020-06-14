from django.conf.urls import url
from user.views import (
    ResentOTPView,OTPVerificationView,
    ChangePasswordView,LoginView,LogoutView,SignUpView
)

urlpatterns = [
    url(r'^signup$', SignUpView.as_view()),
    url(r'^re-sent-otp$', ResentOTPView.as_view()),
    url(r'^otp-verification$', OTPVerificationView.as_view()),
    url(r'^reset-password$', ChangePasswordView.as_view()),
    url(r'^login$', LoginView.as_view()),
    url(r'^logout$', LogoutView.as_view()),
]
