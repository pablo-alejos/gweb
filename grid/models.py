from django.db import models

from django.urls import reverse

class Empleado(models.Model):
    #Fields
    nombre = models.CharField(max_length=220,
                             verbose_name="Nombre de empleado",
                             unique=True)
    status = (
        (None, 'Selecciona estado'),
        ('Baja ', 'Baja'),
        ('Baja temporal', 'Baja temporal'),
        ('Activo', 'Activo'),
    )
    status = models.CharField(max_length=25,
                              choices=status, 
                              verbose_name="Estado de empleado",
                              default="Activo")
    emp_num = models.IntegerField(null=False, unique=True,max_length=10,verbose_name="Numero de empleado")
    email = models.EmailField(blank=True, null=True)

