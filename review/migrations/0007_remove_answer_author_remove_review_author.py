# Generated by Django 4.2.2 on 2023-06-25 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_answer_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='author',
        ),
        migrations.RemoveField(
            model_name='review',
            name='author',
        ),
    ]
