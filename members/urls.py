from django.urls import path
from .views import hello_view, info_view

urlpatterns = [
   path('hello/', hello_view, name='hello_view'),
    path('info/', info_view, name='info_view'),
]