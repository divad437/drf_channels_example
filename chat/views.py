from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse

from .models import Room


def index(request):
    if request.method == "POST":
        name = request.POST.get("name", None)
        if name:
            room = Room.objects.create(name=name)
            return HttpResponseRedirect(reverse("room", args=(room.id,)))
    return render(request, "chat/index.html")


def room(request, room_id):
    room: Room = get_object_or_404(Room, id=room_id)
    return render(request, "chat/room.html", {"room": room})
