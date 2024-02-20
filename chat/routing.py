from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("ws/chat/room/", consumers.RoomConsumer.as_asgi()),
]
