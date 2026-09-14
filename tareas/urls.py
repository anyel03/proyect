
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('crearTareas/', views.crearTareas, name='crearTareas'),
    path('detalleTareas/<int:tarea_id>/', views.detalleTarea, name='detalleTarea'),
    path('eliminarTarea/<int:tarea_id>/',views.eliminarTarea, name='eliminarTarea'),    
]
