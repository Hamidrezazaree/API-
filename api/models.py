from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    content = models.TextField(max_length=500, verbose_name='محتوا')
    author = models.ForeignKey(User,null=True, blank=True, on_delete= models.CASCADE, verbose_name='نویسنده')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده در')

    def __str__(self):
        return self.title