from rest_framework.viewsets import GenericViewSet, ModelViewSet
from users.models import User
from users.serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status



class UserAPIMixin:
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UsersView(UserAPIMixin, ModelViewSet):
     def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
