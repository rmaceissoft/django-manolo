# Generated by Django 2.2.13 on 2020-12-06 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0018_auto_20201128_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='id_number',
            field=models.TextField(db_index=True, help_text='Id number. DNI. It should be char field as some numbers begin with zero.', null=True),
        ),
    ]
