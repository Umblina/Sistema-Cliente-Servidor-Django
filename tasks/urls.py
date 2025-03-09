
from django.urls import path
from .views import task_list, task_create, task_update, task_delete, task_complete

urlpatterns = [
    path('', task_list, name='task_list'),  # Lista de tareas
    path('create/', task_create, name='task_create'),  # Crear tarea
    path('update/<int:pk>/', task_update, name='task_update'),  # Editar tarea
    path('delete/<int:pk>/', task_delete, name='task_delete'),  # Eliminar tarea
    path('complete/<int:pk>/', task_complete, name='task_complete'),  # Completar tarea
]
