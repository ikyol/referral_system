from rest_framework import serializers


class PhoneVerificationSerializer(serializers.Serializer):
    phone_number = serializers.CharField()


class CodeVerificationSerializer(serializers.Serializer):
    verification_code = serializers.CharField(max_length=4)


class UserSerializer(PhoneVerificationSerializer):
    pass


class UserProfileSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    invite_code = serializers.CharField()
    activated_invite_code = serializers.CharField()
    invited_users = UserSerializer(many=True)


class ActivateInviteCodeSerializer(serializers.Serializer):
    invite_code = serializers.CharField()
