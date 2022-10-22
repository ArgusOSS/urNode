from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import LoginAPIView, LogoutAPIView, MeAPIView

urlpatterns = [
    path("login", LoginAPIView.as_view(), name="login"),
    path("logout", LogoutAPIView.as_view(), name="logout"),
    # disabling registration for the time being.
    # path("register", RegisterView.as_view(), name="register"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "me",
        MeAPIView.as_view(),
        name="my-user-info",
    ),
]
