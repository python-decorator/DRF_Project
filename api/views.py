
# myApp/views.py
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.core import serializers
from .models import Task
import json

# myApp/views.py
from rest_framework import viewsets
from .serializers import TaskSerializer

# myApp/views.py
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class TaskViewSet(viewsets.ModelViewSet, APIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # 'django.contrib.auth.User' instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)


class TaskViewXML(View): 
    def get(self, request):
        data = serializers.serialize("xml", Task.objects.all())
        return HttpResponse(data)

# myApp/views.py
class TaskView(View): 
    @method_decorator(csrf_exempt) # Con esto me salto la protección
    def dispatch(self, request, *args, **kwargs):
    # Se ejcuta cada vez que hacemos una petición
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body) # import json
        # print(jd)
        Task.objects.create(
            title=jd['title'],
            description=jd['description'],
            complete=jd['complete']
        )
        datos ={'message': '¡Hecho!'}
        return JsonResponse(datos)
    
    def get(self, request, pk=0):
        if (pk > 0):
            tasks = list(Task.objects.filter(id=pk).values())
            if tasks:
                task = tasks[0]
                datos = {'message': 'Hecho', 'tarea': task}
            else:
                datos ={'message': 'No hay tareas con ese ID'}
        else:
            tasks = list(Task.objects.values())
            if tasks:
                datos ={'message': '¡Hecho!', 'tasks': tasks}
            else:
                datos ={'message': 'No hay tareas'}
        return JsonResponse(datos)    
    
    
    def put(self, request, pk=0):
        jd = json.loads(request.body) # import json
        tasks = list(Task.objects.filter(id=pk).values())
        if tasks:
            task = Task.objects.get(id=pk)
            task.title = jd['title']
            task.description = jd['description']
            task.complete = jd['complete']
            task.save()
            datos = {'message': 'Hecho'}
        else:
            datos = {'message': 'Tarea no encontrada...'}
        return JsonResponse(datos) 

    def delete(self, request, pk=0):
        tasks = list(Task.objects.filter(id=pk).values())
        if tasks:
            Task.objects.filter(id=pk).delete()
            datos = {'message': 'Hecho'}
        else:
            datos = {'message': 'Tarea no encontrada...'}
        return JsonResponse(datos)

