from django.urls import path

from .views import (ActivateInviteCodeView, SendVerificationCodeView,
                    UserProfileView, VerifyCodeAndCreateProfileView)

urlpatterns = [
    path('verification/', SendVerificationCodeView.as_view()),
    path('verify-code/', VerifyCodeAndCreateProfileView.as_view()),
    path('profile/', UserProfileView.as_view()),
    path('activate-invite-code/', ActivateInviteCodeView.as_view())
]
