# Generated by Django 3.1.2 on 2020-11-02 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0010_auto_20201102_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='task_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='task_name',
            field=models.CharField(max_length=100),
        ),
    ]
