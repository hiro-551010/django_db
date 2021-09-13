from django.db import models

class User(models.Model):
    username = models.CharField('ユーザー名', max_length=30)
    password = models.CharField('パスワード', max_length=30)

    class Meta:
        db_table = "User"