from django.db import models
from django.conf import settings
from django.db.models.signals import post_save  # 회원가입과 동시에 프로파일 만들기


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    website_url = models.URLField(blank=True)

def on_post_save_for_user(sender, **kwargs):  # kwargs : instance, created 인자 포함
    if kwargs['created']:
        user = kwargs['instance']
        Profile.objects.create(user=user)

post_save.connect(on_post_save_for_user, settings.AUTH_USER_MODEL)
