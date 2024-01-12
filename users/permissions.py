from rest_framework.permissions import BasePermission
from rest_framework.views import APIView, Request
from users.models import User


class IsOwnerUserOrIsAdmin(BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: User):
        return request.user == obj or request.user.is_superuser


# esse código de cima substitui o de baixo
# class IsAuthenticatedAndIsOwnerUserOrIsAdmin(BasePermission):
#     def has_permission(self, request, view):
#         return (
#             request.user.id == view.kwargs["user_id"]
#             or (request.user.is_superuser)
#         )
