# Generated by Django 2.1.2 on 2018-11-03 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApi', '0004_environment_createtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environment',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 3, 13, 7, 40, 332208)),
        ),
    ]
