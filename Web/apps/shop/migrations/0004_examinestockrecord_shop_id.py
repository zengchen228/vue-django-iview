# Generated by Django 2.1.2 on 2018-12-16 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20181213_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='examinestockrecord',
            name='shop_id',
            field=models.IntegerField(default=2, verbose_name='所属门店'),
            preserve_default=False,
        ),
    ]