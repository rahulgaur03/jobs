# Generated by Django 3.2.8 on 2022-01-10 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsforyou', '0002_auto_20220110_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='lastdate',
            field=models.CharField(default='', max_length=10),
        ),
    ]
