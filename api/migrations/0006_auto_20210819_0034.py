# Generated by Django 3.2.6 on 2021-08-18 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_menu_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='body',
        ),
        migrations.AlterField(
            model_name='menu',
            name='i1',
            field=models.TextField(blank=True, default='Cur Null'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='i2',
            field=models.TextField(blank=True, default='Cur Null'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='i3',
            field=models.TextField(blank=True, default='Cur Null'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='i4',
            field=models.TextField(blank=True, default='Cur Null'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='i5',
            field=models.TextField(blank=True, default='Cur Null'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='i6',
            field=models.TextField(blank=True, default='Cur Null'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='i7',
            field=models.TextField(blank=True, default='Cur Null'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='i8',
            field=models.TextField(blank=True, default='Cur Null'),
        ),
    ]
