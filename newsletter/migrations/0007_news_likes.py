# Generated by Django 2.2.6 on 2020-01-22 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0006_auto_20200121_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]