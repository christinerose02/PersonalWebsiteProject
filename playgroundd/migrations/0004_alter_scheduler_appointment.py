# Generated by Django 4.2 on 2023-05-28 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playgroundd', '0003_scheduler_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduler',
            name='appointment',
            field=models.CharField(max_length=20),
        ),
    ]
