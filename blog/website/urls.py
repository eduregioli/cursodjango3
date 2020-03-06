
from django.urls import path, include
from .views import hello_alugar


urlpatterns = [
    path('', hello_alugar),
    
]
