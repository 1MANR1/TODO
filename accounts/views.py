from rest_framework import generics, permissions
from .models import NewUser
from .serializers import NewUserSerializer

class ListNewUser(generics.ListCreateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer

class DetailNewUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer



    
