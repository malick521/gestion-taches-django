from django.contrib import admin
from django.urls import path
import Task.views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Task.views.homePage, name='home'),
    path('add/', Task.views.addTask, name='add'),
    path('view/', Task.views.viewTask, name='view'),
    path('changeTask/<int:id>', Task.views.changeTask),
    path('deleteTask/<int:id>', Task.views.deleteTask),
]
