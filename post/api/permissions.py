from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "You are not owner!"

    def has_permission(self, request, view):
        # print('has_per')
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # print('obj_perm')
        return obj.user == request.user or request.user.is_superuser
