from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse

from .models import Room


def index(request):
    if request.method == "POST":
        name = request.POST.get("name", None)
        if name:
            room, _ = Room.objects.get_or_create(name=name)
            print(room)
            return HttpResponseRedirect(reverse("chat:room", args=(room.id,)))
    return render(request, "chat/index.html")


def room(request, room_id):
    room: Room = get_object_or_404(Room, id=room_id)
    return render(request, "chat/room.html", {"room": room})
