from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='read_docstring_main'),
]

