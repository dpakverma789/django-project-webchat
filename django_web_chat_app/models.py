from django.db import models
import datetime
import pytz


class ChatRoom(models.Model):
    room_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.room_name


class UserMessage(models.Model):
    time_zone = pytz.timezone('Asia/Kolkata')
    today = datetime.datetime.now(time_zone)
    time_stamp = today.strftime("%I:%M %p %d-%b-%y")
    user_name = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=1000)
    date_time = models.CharField(default=time_stamp, max_length=1000)
    message = models.CharField(max_length=100000)

    def __str__(self):
        return self.user_name
