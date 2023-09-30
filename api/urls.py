
# myApp/urls.py
from django.urls import path, include
from rest_framework import routers
from .views import TaskView, TaskViewXML, TaskViewSet, CustomAuthToken

# myApp/urls.py
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r'tareas', TaskViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Task API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('tasks/', TaskView.as_view(), name='task_list'),
    path('tasks_xml/', TaskViewXML.as_view(), name='task_list_xml'),
    path('tasks/<int:pk>', TaskView.as_view(), name='task_detail'),
    path('', include(router.urls)),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
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

