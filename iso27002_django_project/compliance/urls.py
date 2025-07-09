from django.urls import path
from . import views

app_name = 'compliance'

urlpatterns = [
    path('', views.datos_empresa, name='datos_empresa'),
    path('gestion-controles/', views.gestion_controles, name='gestion_controles'),
    path('evaluacion/', views.evaluacion, name='evaluacion'),
    path('reportes-graficos/', views.reportes_graficos, name='reportes_graficos'),
]
