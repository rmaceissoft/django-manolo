# Generated by Django 3.1.1 on 2020-09-28 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0009_auto_20200927_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='id_number',
            field=models.TextField(help_text='Id number. DNI. It should be char field as some numbers begin with zero.', null=True),
        ),
    ]