# Generated by Django 2.0.7 on 2018-08-07 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20180806_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='reading',
            name='bookId',
            field=models.CharField(default='', max_length=14),
        ),
    ]
