from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, MatriculasViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Alunos', AlunosViewSet, basename='Alunos')
router.register('Cursos', CursosViewSet, basename='Cursos')
router.register('Matriculas', MatriculasViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
