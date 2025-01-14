from django.urls import path

from AppCoder.views import *

urlpatterns = [
    path('', inicio, name='AppCoderInicio'),
    path('curso/', CursoList.as_view(), name='AppCoderCurso'),
    path('entregable/', entregable, name='AppCoderEntregable'),
    path('curso_formulario/', curso_formulario, name='AppCoderCursoFormulario'),
    path('busqueda_camada/', busqueda_camada, name='AppCoderBusquedaCamada'),
    path('busqueda_camada_post/', busqueda_camada_post, name='AppCoderBusquedaCamadaPost'),
    path('eliminar_curso/<int:camada>', eliminar_curso, name='AppCoderEliminarCurso'),
    path('editar_curso/<int:camada>', editar_curso, name="AppCoderEditarCurso")
]
