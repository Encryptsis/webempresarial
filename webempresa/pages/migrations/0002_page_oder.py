# Generated by Django 5.1.1 on 2024-09-27 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='oder',
            field=models.SmallIntegerField(default=0, verbose_name='Orden'),
        ),
    ]
