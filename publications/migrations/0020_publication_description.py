# Generated by Django 2.0.10 on 2019-11-07 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0019_auto_20181019_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание, аннотация'),
        ),
    ]