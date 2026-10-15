from django.urls import path
from .views import index, detalhe, local
urlpatterns = [
    path('', index, name="index"),
    path('evento/<int:id>', detalhe, name="detalhe"),
    path('evento/<int:id>', local, name="local"),
]
