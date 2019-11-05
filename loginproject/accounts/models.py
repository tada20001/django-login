from django.db import models
from django.conf import settings
from django.db.models.signals import post_save  # 회원가입과 동시에 프로파일 만들기
from django.core.mail import send_mail

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    website_url = models.URLField(blank=True)

def on_post_save_for_user(sender, **kwargs):  # kwargs : instance, created 인자 포함
    if kwargs['created']: # created는 처음 생성될때도 호출되고 업데이트될때도 생성됨. 즉 가입시기를 알려줌
        user = kwargs['instance']
        Profile.objects.create(user=user)
        # 이시점에서 환영이메일을 보내줌
        send_mail(
            '가입환영',
            '환영합니다.',
            'from@exmaple.com',
            [user.email],
            fail_silently=False,
        )

# 1. 회원가입 탐지
post_save.connect(on_post_save_for_user, settings.AUTH_USER_MODEL)
