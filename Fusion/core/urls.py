from django.urls import path 

from .views import IndexView, atualiza_estoque

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('teste/<int:id>', atualiza_estoque, name='teste')
]