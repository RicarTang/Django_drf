from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from rest_framework import status


# Create your views here.
@api_view(["GET"])
def users(request):
    users = User.objects.all()
    ser = UserSerializer(users, many=True)
    return Response(
        {"code": 200, "data": ser.data, "message": "OK"}, status=status.HTTP_200_OK
    )


@api_view(["POST"])
def create(request):
    ser = UserSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(
            {"code": 201, "data": ser.data, "message": "OK"},
            status=status.HTTP_201_CREATED,
        )
    return Response(
        {"code": 400, "message": ser.errors},
        status=status.HTTP_400_BAD_REQUEST,
    )
