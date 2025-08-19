# finanzas/context_processors.py

from .models import Ingreso, Gasto
from django.db.models import Sum

def saldo_actual(request):
    if request.user.is_authenticated:
        total_ingresos = Ingreso.objects.filter(user=request.user).aggregate(Sum('cantidad'))['cantidad__sum'] or 0
        total_gastos = Gasto.objects.filter(user=request.user).aggregate(Sum('cantidad'))['cantidad__sum'] or 0
        saldo = total_ingresos - total_gastos
    else:
        saldo = 0
    return {'saldo_actual': saldo}