from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserRegistrationView, TodoViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('todos', TodoViewSet, basename="todo")

custom_patterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = router.urls + custom_patterns