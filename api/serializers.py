from rest_framework import serializers
from auth_api.models import User
from .models import Tag, Blog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'name')
        extra_kwargs = { 'password': { 'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')



class BlogSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    username = serializers.ReadOnlyField(source='user.name', read_only=True) #userの名前を表示させる。

    class Meta:
        model = Blog
        fields = ('id', 'title', 'user', 'username', 'tags', 'content', 'is_active', 'image', 'created_at')

class BlogCreateSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    username = serializers.ReadOnlyField(source='user.name', read_only=True)  # userの名前を表示させる。


    class Meta:
        model = Blog
        fields = ('id','title' ,'user' ,'username','tags','content','is_active','image', 'created_at')