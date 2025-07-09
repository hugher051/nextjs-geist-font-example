from django.db import models

class Company(models.Model):
    nombre = models.CharField(max_length=255)
    sector_industrial = models.CharField(max_length=255)
    contacto_principal = models.CharField(max_length=255)
    fecha_evaluacion = models.DateField()
    observaciones_generales = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Control(models.Model):
    TIPO_CONTROL_CHOICES = [
        ('tipo1', 'Tipo 1'),
        ('tipo2', 'Tipo 2'),
        ('tipo3', 'Tipo 3'),
    ]
    tipo_control = models.CharField(max_length=50, choices=TIPO_CONTROL_CHOICES)
    clausula = models.CharField(max_length=100, blank=True)
    titulo_requerimiento = models.CharField(max_length=255)
    detalle_control = models.TextField()

    def __str__(self):
        return self.titulo_requerimiento

class Evaluacion(models.Model):
    CALIFICACION_CHOICES = [
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja'),
    ]
    control = models.ForeignKey(Control, on_delete=models.CASCADE)
    calificacion = models.CharField(max_length=50, choices=CALIFICACION_CHOICES)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    responsable = models.CharField(max_length=255)
    tiene_documentacion_formal = models.BooleanField()
    documentacion_referencia = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Evaluacion de {self.control.titulo_requerimiento}"
