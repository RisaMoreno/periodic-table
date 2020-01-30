from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('atom/<int:atomic_num>', views.show_atom),
]