# Generated by Django 3.2.8 on 2023-02-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20221214_0138'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='term',
            field=models.DateField(null=True, verbose_name='期限'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=30, verbose_name='タスク'),
        ),
    ]
