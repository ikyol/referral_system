import random
import string
import time

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (ActivateInviteCodeSerializer,
                          CodeVerificationSerializer,
                          PhoneVerificationSerializer, UserProfileSerializer)

User = get_user_model()


class SendVerificationCodeView(APIView):
    def post(self, request):
        serializer = PhoneVerificationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        verification_code = ''.join(random.choices(string.digits, k=4))

        phone_number = serializer.validated_data.get('phone_number')
        user, created = User.objects.get_or_create(phone_number=phone_number)
        if created:
            user.set_unusable_password()
            user.generate_invite_code()

        user.activation_code = verification_code
        user.save()

        # Imitation delay
        time.sleep(random.uniform(1, 2))

        return Response({'data': {
            'verification_code': verification_code
        }}, status=status.HTTP_200_OK)


class VerifyCodeAndCreateProfileView(APIView):
    def post(self, request):
        serializer = CodeVerificationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        verification_code = serializer.validated_data.get('verification_code')

        users = User.objects.filter(activation_code=verification_code)
        if not users.exists():
            return Response({'data': {
                'message': 'Incorrect code'
            }}, status=status.HTTP_400_BAD_REQUEST)

        user = users.first()
        user.activation_code = None
        user.save()
        token, created = Token.objects.get_or_create(user=user)

        return Response({'data': {
            'token': token.key
        }}, status=status.HTTP_201_CREATED)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        invited_users = User.objects.filter(activated_invite_code=user.invite_code)

        serializer = UserProfileSerializer({
            'phone_number': user.phone_number,
            'invite_code': user.invite_code,
            'activated_invite_code': user.activated_invite_code,
            'invited_users': invited_users
        })
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)


class ActivateInviteCodeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        if user.activated_invite_code:
            return Response({'data': {
                'message': "You're already used invite code"
            }}, status.HTTP_403_FORBIDDEN)

        serializer = ActivateInviteCodeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        invite_code = serializer.validated_data.get('invite_code')

        if user.invite_code == invite_code:
            return Response({'data': {
                'message': 'You cannot use your invite code'
            }}, status.HTTP_403_FORBIDDEN)

        users = User.objects.filter(invite_code=invite_code)
        if not users.exists():
            return Response({'data': {
                'message': 'Incorrect invite code'
            }}, status=status.HTTP_400_BAD_REQUEST)

        user.activated_invite_code = invite_code
        user.save()

        return Response({'data': {
            'message': 'Invite code Activated'
        }}, status.HTTP_200_OK)
