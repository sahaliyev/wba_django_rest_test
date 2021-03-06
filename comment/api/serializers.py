from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from comment.models import Comment
from rest_framework import serializers
from post.models import Post


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('created',)

    def validate(self, attrs):
        if attrs['parent']:
            if attrs['parent'].post != attrs['post']:
                raise serializers.ValidationError("wrong")
        return attrs


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentListSerializer(ModelSerializer):
    replies = SerializerMethodField()
    user = UserSerializer()
    post = PostSerializer()

    class Meta:
        model = Comment
        fields = '__all__'
        # depth = 1  # serialize all fk fields

    def get_replies(self, obj):
        if obj.any_children:
            return CommentListSerializer(obj.children(), many=True).data


# class CommentChildSerializer(ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'
class CommentDeleteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']
