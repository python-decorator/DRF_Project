
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task


class TaskAPITests(APITestCase):

    def test_post_task(self):
        url = '/api/tareas/'
        data = {'title': 'Test Task', 'description':'Test Description', 'complete':False}
        response = self.client.post(url, data, format='json')
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')


    def test_get_tasks(self):
        Task.objects.create(title=f'Tarea de prueba 1',description=f'Description Prueba 1',complete= False)
        Task.objects.create(title=f'Tarea de prueba 2',description=f'Description Prueba 2',complete= True)
        response = self.client.get('/api/tareas/')
        response_json = response.json()
        # print(response_json)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_json), 2)
        self.assertIsInstance(response_json, list)
        self.assertIsInstance(response_json[0], dict)
        self.assertIsInstance(response_json[1], dict)

    
    def test_get_task(self):
        Task.objects.create(title=f'Tarea de prueba 1',description=f'Description Prueba 1',complete= False)
        Task.objects.create(title=f'Tarea de prueba 2',description=f'Description Prueba 2',complete= True)
        url = '/api/tareas/1/'
        response = self.client.get(url)
        response_json = response.json()
        # print(response_json)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_json), 5)
        self.assertIsInstance(response_json.get('id'), int)
        self.assertIsInstance(response_json.get('title'), str)
        self.assertIsInstance(response_json.get('description'), str)
        self.assertIsInstance(response_json.get('complete'), bool)

    # def _authenticate(self):
    #     user = User.objects.create(username='admin', password='admin')
    #     token = Token.objects.create(user=user)
    #     # token = Token.objects.get(user__username='admin')
    #     client = APIClient()
    #     client.force_authenticate(user=user)
    #     client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    #     print(user.is_authenticated)