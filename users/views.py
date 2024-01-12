from rest_framework.views import APIView, Request, Response, status
from users.serializers import UserSerializer
from users.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsOwnerUserOrIsAdmin
from rest_framework.generics import get_object_or_404


class UserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class UserIdView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerUserOrIsAdmin]

    def get(self, request: Request, user_id: int) -> Response:
        found_user = get_object_or_404(User.objects.all(), id=user_id)
        # essa linha de cima substitui essas debaixo
        # try:
        #     found_user = User.objects.get(id=user_id)
        # except User.DoesNotExist:
        #     return Response({"detail": "Not found."}, status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(request, found_user)
        serializer = UserSerializer(found_user)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, user_id: int) -> Response:
        found_user = get_object_or_404(User.objects.all(), id=user_id)
        self.check_object_permissions(request, found_user)
        serializer = UserSerializer(found_user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
