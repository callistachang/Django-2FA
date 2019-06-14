import uuid
from rest_framework import views, permissions, status
from rest_framework.response import Response

class SpaUserLogoutAllView(views.APIView):
    """
    Use this endpoint to log out all sessions for a given user.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        user.jwt_secret = uuid.uuid4()
        user.save()
        
        return Response(status=status.HTTP_204_NO_CONTENT)

from djoser.views import UserView, UserDeleteView
from djoser import serializers
from rest_framework import permissions
from SpaApp.models import SpaUser
from OtpApp import permissions as otp_permissions

class SpaUserView(UserView):
    """
    Uses the default Djoser view, but add the IsOtpVerified permission.
    Use this endpoint to retrieve/update user.
    """
    model = SpaUser
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated, otp_permissions.IsOtpVerified]
 
class SpaUserDeleteView(UserDeleteView):
    """
    Uses the default Djoser view, but add the IsOtpVerified permission.
    Use this endpoint to remove actually authenticated user.
    """
    serializer_class = serializers.UserDeleteSerializer
    permission_classes = [permissions.IsAuthenticated, otp_permissions.IsOtpVerified]
