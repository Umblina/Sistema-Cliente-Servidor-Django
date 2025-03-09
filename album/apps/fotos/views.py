from django.shortcuts import render
from .models import Mifoto


def fotos(request):
    mis_fotos = Mifoto.objects.all()
    return render(request,"pages/fotos.html",{"fotos":mis_fotos})