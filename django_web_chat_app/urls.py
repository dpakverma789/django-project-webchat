from django.urls import path, include
from django_web_chat_app import views

urlpatterns = [
    # path(route,view,kwargs,name)
    path('', views.home, name='chat-home'),
    path('chatroom', views.chat_room, name='chat-room'),
    path('<str:room>/', views.room, name='room'),
    path('send', views.send_msg, name='chat-msg'),
    path('getMessages/<str:room>', views.fetch_messages, name='fetch-msg'),
]

# handler404 = "passwordManager.views.page_not_found_view"