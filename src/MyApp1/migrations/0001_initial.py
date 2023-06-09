# Generated by Django 4.2 on 2023-04-16 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Ф.И.О.')),
                ('mail', models.CharField(max_length=128, verbose_name='Эл. почта')),
                ('phone', models.CharField(max_length=12, verbose_name='Телефон')),
                ('message', models.CharField(max_length=256, verbose_name='Сообщение')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
        ),
    ]
