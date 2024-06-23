from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('join', index),
    path('create-room', index),
    # Format to write query parameter related URL's
    path('room/<str:roomCode>', index),
]