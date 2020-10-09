from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser # AbstractUser : 기존의 User 모델을 사용하되, 추가적인 정보를 더 넣고 싶을 때 사용. 

# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    nickname=models.CharField(max_length=100)
    age= models.PositiveIntegerField(null=True, blank=True)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='following')
