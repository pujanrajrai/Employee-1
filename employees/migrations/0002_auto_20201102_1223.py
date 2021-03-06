# Generated by Django 3.1.2 on 2020-11-02 06:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='employee_gender',
        ),
        migrations.AddField(
            model_name='employee',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
