from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'uid', 'nm_user', 'email', 'address', 'number', 'city', 'state','created' )