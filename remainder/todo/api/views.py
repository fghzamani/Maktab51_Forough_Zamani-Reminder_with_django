from rest_framework.generics import ListAPIView
from todo.models import Task
from .selializers import TaskSerializer

class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer