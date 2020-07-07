from django.urls import path
from . import views
# app = 'update'
urlpatterns = [
    path('update_task/<int:pk>/', views.updateTask, name="update_task"),
]
