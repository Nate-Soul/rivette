"""proj07 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('todo/add/', views.addNewTask, name='add'),
    path('todo/<int:todo_id>/complete', views.completeTask, name='complete'),
    path('todo/<int:todo_id>/reset', views.resetCompletedTask, name='reset'),
    path('todo/<int:todo_id>/remove', views.deleteTask, name='remove'),
    path('todo/remove-completed/', views.deleteCompletedTasks, name='deletes'),
    path('todo/complete-all/', views.completeTasks, name='completes'),
    path('todo/reset-all/', views.resetCompletedTasks, name='resets'),
]

handler404 = 'todolist.views.error_404'