from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Tarea




def index(request):
    Tareas = Tarea.objects.all()
    return render(request, 'index.html',{'Tareas': Tareas })


def crearTareas(request):
    if request.method == 'GET':
        return render(request, 'crearTareas.html')
    else:
        try:
            print(request.POST)
            
            tarea = Tarea(
                titulo=request.POST['titulo'],
                descripcion = request.POST.get('descripcion', ''),
                importante = request.POST.get('importante') == 'on',
            )
            tarea.save()
            return redirect('index')
        except ValueError as e:
            return render(request, 'crearTareas.html',{
                'error' : e
            })

        
def detalleTarea(request, tarea_id):
    if request.method == 'GET':
        tarea = get_object_or_404(Tarea,pk=tarea_id)
        return render(request, 'detalleTarea.html', {'tarea': tarea})
    else: 
        try:
            tarea = get_object_or_404(Tarea,pk=tarea_id)
            tarea.titulo = request.POST['titulo']
            tarea.descripcion = request.POST.get('descripcion')
            tarea.importante = request.POST.get('importante') == 'on'
            tarea.save()
            return redirect('index')
        except ValueError as e:
            return render(request, 'detalleTarea.html',{
                'tarea': tarea,
                'error' : e
            })

def eliminarTarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    tarea.delete()
    return redirect('index')