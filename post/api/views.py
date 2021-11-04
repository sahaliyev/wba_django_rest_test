from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import PostPagination
from post.api.permissions import IsOwner
from post.models import Post
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, \
    CreateAPIView, RetrieveUpdateAPIView
from post.api.serializers import PostSerializers, PostUpdateCreateSerializers
from rest_framework.permissions import (IsAuthenticated, IsAdminUser)


class PostListAPIView(ListAPIView):
    # queryset = Post.objects.all()
    serializer_class = PostSerializers
    filter_backends = [SearchFilter, OrderingFilter]
    pagination_class = PostPagination
    search_fields = ['title']

    def get_queryset(self):
        queryset = Post.objects.filter(draft=False)
        return queryset


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'
    permission_classes = [IsOwner, IsAdminUser]


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateCreateSerializers
    lookup_field = 'slug'
    permission_classes = [IsOwner, IsAdminUser]

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateCreateSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
