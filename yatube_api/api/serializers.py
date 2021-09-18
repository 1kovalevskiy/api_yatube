from django.contrib.auth import get_user_model
from rest_framework import serializers
from posts.models import Post, Group, Comment


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class PostSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(
    #     read_only=True, default=serializers.CurrentUserDefault())
    # author = UserSerializer(read_only=True)
    # author = serializers.SerializerMethodField(read_only=True)
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = '__all__'

    # def get_author(self, obj):
    #     return obj.author.get_fields('username')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = '__all__'
