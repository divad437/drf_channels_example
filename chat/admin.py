from django.contrib import admin

from .models import Message, Room, User

admin.site.register(Room)
admin.site.register(User)
admin.site.register(Message)
