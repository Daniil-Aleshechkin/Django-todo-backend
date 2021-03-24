from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from ..models import Task
from .serializers import TaskSerializer


@api_view(["GET", ])
def api_detail_task_view(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user

    if task.author != user:

        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "GET":
        serializer = TaskSerializer(task)
        return Response(serializer.data)


@api_view(["GET", ])
def api_detailall_task_view(request):
    try:
        task = Task.objects.filter(author=request.user)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)


@api_view(["PUT", ])
def api_update_task_view(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user

    if task.author != user:

        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "PUT":
        serializer = TaskSerializer(task, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE", ])
def api_delete_task_view(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user

    if task.author != user:

        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "DELETE":
        operation = task.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"

        return Response(data=data)


@api_view(["POST", ])
def api_create_task_view(request):

    account = request.user

    task = Task(author=account)
    if request.method == "POST":
        serializer = TaskSerializer(task, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'id': task.id},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
