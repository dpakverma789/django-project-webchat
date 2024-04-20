from django.shortcuts import render, redirect
from django_web_chat_app.models import ChatRoom, UserMessage
from django.http import HttpResponse, JsonResponse


def home(request):
    return render(request, 'home.html')


def room(request, room):
    user_name = request.GET.get('username')
    if user_name:
        room_details = ChatRoom.objects.get(room_name=room)
        return render(request, 'room.html',
                      {'room': room,
                       'username': user_name,
                       'room_details': room_details
                       })


def chat_room(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        user_name = request.POST.get('username')
        if not ChatRoom.objects.filter(room_name=room_name).exists():
            chat = ChatRoom()
            chat.room_name = room_name
            chat.save()
            return redirect('/'+room_name+'/?username='+user_name)
        else:
            return redirect('/'+room_name+'/?username='+user_name)


def send_msg(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        user_name = request.POST.get('username')
        message = request.POST.get('message')
        if message:
            chat = UserMessage.objects.create(message=message, user_name=user_name, room_name=room_id)
            chat.save()
        return True
    return False


def fetch_messages(request, room):
    if room:
        chats = UserMessage.objects.filter(room_name=room)
        return JsonResponse({"messages":list(chats.values())})
