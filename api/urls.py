
# myApp/urls.py
from django.urls import path, include
from rest_framework import routers
from .views import TaskView, TaskViewXML, TaskViewSet, CustomAuthToken

router = routers.DefaultRouter()
router.register(r'tareas', TaskViewSet)

urlpatterns = [
    path('tasks/', TaskView.as_view(), name='task_list'),
    path('tasks_xml/', TaskViewXML.as_view(), name='task_list_xml'),
    path('tasks/<int:pk>', TaskView.as_view(), name='task_detail'),
    path('', include(router.urls))
]

# myApp/urls.py
# Crear una ruta para cada usuario creado solicite su token
# enviando la petición POST desde un FORMULARIO o JSON
from rest_framework.authtoken import views
urlpatterns += [
    #path('api-token-auth/', views.obtain_auth_token)
    # myApp/urls.py. Modificar e importar vista
    path('api-token-auth/', CustomAuthToken.as_view())
]



# import base64
# encoded = base64.b64encode(b'admin:admin')
# print(encoded)
# b'YWRtaW46YWRtaW4='

# Crear un token para cada usuario
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token

# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)

