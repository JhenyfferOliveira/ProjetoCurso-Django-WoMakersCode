from django.urls import path
from cursos.views import criar_curso, inicio_curso

app_name = 'Cursos'
urlpatterns =[
    path('inicio_curso/', inicio_curso, name="inicio_curso"),
    path('criar_curso/', criar_curso, name='criar_curso')
]