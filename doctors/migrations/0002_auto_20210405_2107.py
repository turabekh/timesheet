# Generated by Django 3.1.7 on 2021-04-06 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='work_date',
            field=models.DateField(),
        ),
    ]