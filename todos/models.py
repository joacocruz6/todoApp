from django.db import models
from datetime import date
# Create your models here.

class ProyectoTodo(models.Model):
    """
    Modelo que representa un proyecto del usuario
    
    Attributes:
        nombre {CharField} -- Nombre del proyecto
    """
    nombre = models.CharField(max_length=255,primary_key=True)


class Categoria(models.Model):
    """
    Categoria que tienen las tareas
    
    Attributes:
        nombre {CharField} -- Nombre de la categoria.
    """
    nombre = models.CharField(max_length=255, primary_key=True)


class Tarea(models.Model):
    """
    Modelo que representa una tarea en el proyecto
    
    Attributes:
        nombre {CharField} -- Nombre de la tarea a realizar
        estado {BooleanField} -- True si la tarea está terminada.
        fecha_inicio {DateField} -- Fecha en que la tarea fue iniciada, por default es el dia de la creacion.
        fecha_final {DateField} -- Fecha en que la tarea debe ser finalizada, puede no ser ingresada o no tener.
        proyecto_asociado {ForeignKey} -- Proyecto al cual esta vinculada la tarea. 
    """
    nombre = models.CharField(max_length=255)
    estado = models.BooleanField(default=False)
    fecha_inicio = models.DateField(default=date.today())
    fecha_final = models.DateField(null=True)
    proyecto_asociado = models.ForeignKey(
        ProyectoTodo, on_delete=models.CASCADE)
    categorias_catalogadas = models.ManyToManyField(Categoria)

