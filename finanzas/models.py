from django.db import models
from django.contrib.auth.models import User

class Ingreso(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()
    concepto = models.CharField(max_length=200)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.fecha} - {self.concepto}: +{self.cantidad} €"

class Gasto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()
    concepto = models.CharField(max_length=200)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.fecha} - {self.concepto}: -{self.cantidad} €"
