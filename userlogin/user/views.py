from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import Response
from .models import User
from rest_framework.exceptions import AuthenticationFailed
class RagisterView(APIView):
    def post(self, request):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('user not found')

        if not user.check_password('password'):
            raise AuthenticationFailed('incorrect password')

        return Response({'massage ': 'success'})
