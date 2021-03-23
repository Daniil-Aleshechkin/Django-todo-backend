from django.urls import path

from .views import (
    api_detail_task_view,
    api_detailall_task_view,
    api_update_task_view,
    api_delete_task_view,
    api_create_task_view
)

app_name = 'todo'

urlpatterns = [
    path('<id>',api_detail_task_view,name="task_detail"),
    path('all/',api_detailall_task_view,name="task_detailall"),
    path('<id>/update/',api_update_task_view,name="task_update"),
    path('<id>/delete/',api_delete_task_view,name="task_delete"),
    path('create/',api_create_task_view,name="task_create"),
]