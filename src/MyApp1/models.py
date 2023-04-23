from django.db import models

class Request(models.Model):
    name = models.CharField(max_length=128, verbose_name='Ф.И.О.', blank=False)
    mail = models.CharField(max_length=128, verbose_name='Эл. почта',blank=False)
    phone = models.CharField(max_length=20, verbose_name='Телефон',blank=False)
    message = models.TextField(max_length=256, verbose_name='Сообщение',blank=False)
    date = models.CharField(max_length=11, verbose_name='Дата создания', blank=True)

    def __str__(self):
        return 'Заявка от ' + self.name + ', Дата: ' + self.date
class Comment(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя', blank=False)
    message = models.TextField(max_length=256, verbose_name='Отзыв', blank=False)
    date = models.CharField(max_length=11, verbose_name='Дата отправки', blank=True)

    def __str__(self):
        return 'Комментарий от ' + self.name + ', Дата: ' + self.date