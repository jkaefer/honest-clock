# serializers.py
from rest_framework.serializers import ModelSerializer

from .models import Times,Users

class TimesSerializer(ModelSerializer):
    class Meta:
        model = Times
        fields = (
            'username','time_punch','site_address'
        )

class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'username','password'
        )

