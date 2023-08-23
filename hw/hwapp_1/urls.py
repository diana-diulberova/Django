from django.urls import path
from . import views

urlpatterns = [
    path('', views.general, name='general'),
    path('about/', views.about, name='about'),
]
