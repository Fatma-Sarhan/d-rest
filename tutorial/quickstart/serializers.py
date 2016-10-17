from django.contrib.auth.models import User, Group 
from rest_framework import serializers
from datetime import datetime
from .models import Comment




class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email','password','first_name', 'groups','is_staff')

    def create(self, validated_data):
	    user = User(
	        first_name = validated_data['first_name'],
	        username = validated_data['username'],
	        email = validated_data['email'],
	        is_staff = validated_data['is_staff']

	    )
	    user.set_password(validated_data['password'])
	    user.save()
	    return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')



class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('url', 'content','created','user_id')
