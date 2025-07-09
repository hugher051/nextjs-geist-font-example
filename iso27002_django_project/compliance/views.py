from django.shortcuts import render

def datos_empresa(request):
    return render(request, 'compliance/datos_empresa.html')

def gestion_controles(request):
    return render(request, 'compliance/gestion_controles.html')

def evaluacion(request):
    return render(request, 'compliance/evaluacion.html')

def reportes_graficos(request):
    return render(request, 'compliance/reportes_graficos.html')
