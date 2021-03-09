from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

class LoginUser(models.Model):

    user_id = models.CharField(max_length=20, unique=True, null=False, default='')
    user_pw = models.CharField(max_length=256, null=False, default=False)

    name = models.CharField(verbose_name="이름", max_length=20, null=False, default='')
    birth_day = models.DateField(verbose_name="생년월일", null=True)
    gender = models.CharField(verbose_name="성별", max_length=6, null=False, default="Male")
    email = models.EmailField(verbose_name="이메일 주소", max_length=30, null=False, default='')
    age = models.IntegerField(verbose_name="나이", default=3)

    class Meta:
        db_table = 'login_user'
        verbose_name = '로그인 테스트 테이블'