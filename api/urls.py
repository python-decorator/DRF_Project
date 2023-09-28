
# myApp/urls.py
from django.urls import path, include
from rest_framework import routers
from .views import TaskView, TaskViewXML, TaskViewSet

router = routers.DefaultRouter()
router.register(r'tareas', TaskViewSet)

urlpatterns = [
    path('tasks/', TaskView.as_view(), name='task_list'),
    path('tasks_xml/', TaskViewXML.as_view(), name='task_list_xml'),
    path('tasks/<int:pk>', TaskView.as_view(), name='task_detail'),
    path('', include(router.urls))
]

import base64
encoded = base64.b64encode(b'admin:admin')
print(encoded)
b'YWRtaW46YWRtaW4='



