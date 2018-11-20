# Generated by Django 2.1.2 on 2018-11-19 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='名称')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='common.Genre', verbose_name='所属类别')),
            ],
            options={
                'verbose_name': '类别',
                'verbose_name_plural': '类别',
                'db_table': 'common_genre',
            },
        ),
        migrations.AlterField(
            model_name='quantify',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='单位'),
        ),
    ]