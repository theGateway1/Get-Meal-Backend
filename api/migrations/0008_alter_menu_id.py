# Generated by Django 3.2.6 on 2021-08-24 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210820_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
