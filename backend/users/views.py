# Create your views here.
from rest_framework import generics, viewsets
from .serializers import UserSerializer, TodoSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated] #Endpoint Protection

    def get_queryset(self):
        return self.request.user.todo_set.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)