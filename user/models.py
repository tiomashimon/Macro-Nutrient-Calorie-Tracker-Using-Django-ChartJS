# models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    calories_goal = models.IntegerField(default=2000)

    def __str__(self):
        return self.user.username


# Подключаем обработчик сигнала
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_data(sender, instance, created, **kwargs):
    if created:
        UserData.objects.create(user=instance)
