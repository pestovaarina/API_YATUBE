from rest_framework import (viewsets, permissions,
                            mixins, filters)
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404

from .permissions import IsOwner
from posts.models import Post, Group
from .serializers import (PostSerializer, GroupSerializer,
                          CommentSerializer, FollowSerializer)


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet для обьектов модели Post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwner,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Создает запись, где автором является текущий пользователь."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для обьектов модели Group."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsOwner,)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для обьектов модели Comment."""

    serializer_class = CommentSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        """Возвращает queryset c комментариями для текущей записи."""
        post_id = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post_id.comments

    def perform_create(self, serializer):
        """Создает комментарий для текущего поста.

        Автором является текущий пользователь.
        """
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(post=post, author=self.request.user)


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Вьюсет для обьектов модели Follow."""

    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        """Возвращает queryset c подписками для текущего пользователя."""
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        """Создает подписку, где подписчиком является текущий пользователь."""
        serializer.save(user=self.request.user)
