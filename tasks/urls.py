from django.urls import path
from tasks.views import create_task, get_task_status

urlpatterns = [
    path('api/create-task/', create_task, name='create_task'),
    path('api/get-task-status/<int:task_id>/', get_task_status, name='get_task_status'),
]