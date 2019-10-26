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


