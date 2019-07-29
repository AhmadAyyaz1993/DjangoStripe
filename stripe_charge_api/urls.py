from django.urls import path
from . import views


urlpatterns = [
    path('api/charge/', views.charge),
]
