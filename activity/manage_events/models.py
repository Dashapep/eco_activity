from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Events(models.Model):
    title = models.CharField(max_length=50, verbose_name='Событие')
    image = models.ImageField(upload_to='image', verbose_name='Картинка', blank=True)
    content = models.TextField(max_length=1500, verbose_name='Описание события')
    file_field = models.FileField(upload_to='file', verbose_name='Файл')
    is_urgent = models.BooleanField(default=False, verbose_name='Срочно')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    tags = models.ManyToManyField('Tag', verbose_name='Теги')

    def get_tags(self):
        tags_li = self.tags.all()
        res = []
        for tag in tags_li:
            res.append(tag.title)
        return ', '.join(res)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Событие'
        verbose_name = 'События'

class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тег')
    date_created = models.DateTimeField(auto_now_add='True')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'