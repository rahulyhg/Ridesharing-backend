from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserProfile, Bank

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username','first_name','last_name','email','last_login','date_joined','is_active')


class BasicUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username','first_name','last_name','email')

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ('__all__')

class UserProfileSerializer(serializers.ModelSerializer):
    bank = BankSerializer(read_only=True)
    user = BasicUserDataSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = ('__all__')

class UserProfileByUserSerializer(serializers.ModelSerializer):
    #bank = BankSerializer(read_only=True)
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())
    class Meta:
        model = UserProfile
        fields = ('__all__')


class UserProfileViewByUserSerializer(serializers.ModelSerializer):
    bank = BankSerializer(read_only=True)
    user = BasicUserDataSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = ('__all__')