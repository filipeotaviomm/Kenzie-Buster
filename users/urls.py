from django.urls import path
from users.views import UserView, UserIdView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<int:user_id>/", UserIdView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
    # path("token/refresh/", views.TokenRefreshView.as_view()),
]
