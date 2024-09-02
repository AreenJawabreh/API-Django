from django.urls import path
from .views import hello_view, info_view

urlpatterns = [
    path('info/', info_view),
    path('hello/', hello_view),
]