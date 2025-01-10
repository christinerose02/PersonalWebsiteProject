# Generated by Django 4.2 on 2023-05-29 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playgroundd', '0004_alter_scheduler_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='VeterinaryScheduler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cellnumber', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=50)),
                ('pettype', models.CharField(max_length=20)),
                ('appointment', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]