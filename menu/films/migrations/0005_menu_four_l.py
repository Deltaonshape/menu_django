# Generated by Django 4.1.5 on 2023-01-26 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='four_l',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
