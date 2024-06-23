#Adding app name is compulsory otherwise migrations will throw an error
# erro ref => https://stackoverflow.com/questions/68145060/django-makemigrations-module-object-is-not-iterable 
from django.urls import path
from .views import RoomView, CreateRoomView, GetRoom

app_name="api"

urlpatterns = [
  path('home', RoomView.as_view()),
  path('create-room', CreateRoomView.as_view()),
  path('get-room', GetRoom.as_view())
]