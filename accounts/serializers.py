from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

User = get_user_model()

# Custom serializer for registering a user
class CustomUserCreateSerializer(UserCreateSerializer):
    message = serializers.SerializerMethodField()
    
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 
                'password', 're_password', 'message')
        extra_kwargs = {
            'password': {'write_only': True},
            're_password': {'write_only': True}
        }

# Custom serializer for retrieving a profile of a user
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'role', 'is_active', 'date_joined')
        read_only_fields = ('role', 'is_active', 'date_joined')