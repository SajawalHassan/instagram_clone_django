# Generated by Django 3.2.9 on 2021-11-15 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211115_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
