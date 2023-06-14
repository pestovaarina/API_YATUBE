from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Изменять и удалять контент можно только автору.
    Неавторизованному пользлвателю доступно только чтение."""

    message = 'Изменение и удаление чужого контента запрещено!'

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
