from rest_framework import serializers
from post.models import Post


class PostSerializers(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='post:detail', lookup_field='slug')
    username = serializers.SerializerMethodField(method_name='username_new')

    class Meta:
        model = Post
        fields = ['id', 'username', 'title', 'content', 'image', 'url', 'created', 'modified_by']

    def username_new(self, obj):
        return str(obj.user.username)


class PostUpdateCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

    # def save(self, **kwargs):
    #     print('test')
    #     return True

    # def create(self, validated_data):
    #     assign user to post
    #     return Post.objects.create(user=self.context['request'].user, **validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     return instance

    # def validate_title(self, value):
    #     # validate each filed separately
    #     if value == 'akif':
    #         raise serializers.ValidationError("olmaz")
    #     return value

    # def validate(self, attrs):
    #     # all data
    #     print(attrs['title'])
    #     return attrs
