# Generated by Django 2.2 on 2020-06-21 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200621_1421'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='twisteduser',
            options={'verbose_name_plural': 'users'},
        ),
    ]