# Generated by Django 2.1.2 on 2018-12-12 10:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0002_auto_20181212_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xyuser',
            name='name',
        ),
        migrations.AlterField(
            model_name='xyuser',
            name='email',
            field=models.EmailField(blank=True, db_index=True, max_length=50, null=True, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='邮箱地址'),
        ),
        migrations.AlterField(
            model_name='xyuser',
            name='first_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MaxLengthValidator(30)], verbose_name='姓'),
        ),
        migrations.AlterField(
            model_name='xyuser',
            name='last_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MaxLengthValidator(30)], verbose_name='名'),
        ),
    ]