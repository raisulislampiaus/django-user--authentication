from email import message
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .products import products
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer,UserSerializerWithToken
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# Create your views here.
from rest_framework import status


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
     def validate(self, attrs):
        data = super().validate(attrs)

        serialize = UserSerializerWithToken(self.user).data
        for k, v in serialize.items():
            data[k] = v
        

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




@api_view(['POST'])


def userRegister(request):
    data = request.data 
    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )
        serialize = UserSerializerWithToken(user, many=False)
        return Response(serialize.data)
    except:
        message = {'details': 'User email already exits'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
     

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUser(request):
    user = request.user
    serialize = UserSerializer(user, many=False)
    return Response(serialize.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serialize = UserSerializer(users, many=True)
    return Response(serialize.data)


@api_view(['GET'])
def getRoutes(request):
    return Response('hellow piaus')

@api_view(['GET'])
def getProducts(request):
    return Response(products)

@api_view(['GET'])
def getProduct(request, pk):
    product = None
    for i in products:
       if i['_id'] == pk:
           product = i
           break
    return Response(product)
    
