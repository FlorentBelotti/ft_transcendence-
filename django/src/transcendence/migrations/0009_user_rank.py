# Generated by Django 4.2 on 2025-02-06 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcendence', '0008_verificationcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
