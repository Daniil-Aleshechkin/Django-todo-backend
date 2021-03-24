from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from account.api.serializers import AccountSerializer
from rest_framework.authtoken.models import Token


@api_view(['POST'])
@permission_classes([AllowAny])
def api_create_account_view(request):

    if request.method == "POST":
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            data = {}
            data['response'] = 'successfully created user'
            data['email'] = account.email
            data['username'] = account.username
            data['token'] = Token.objects.get(user=account).key
        else:
            data = serializer.errors
        return Response(data=data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_detail_account_view(request):

    if request.method == "GET":
        account = request.user
        data = {}
        data['email'] = account.email
        data['username'] = account.username
        return Response(data=data)
