# Generated by Django 2.0.7 on 2018-07-29 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0006_auto_20180729_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='host_title',
            field=models.TextField(help_text='Official title of host: Jefe, Director, etc', null=True),
        ),
    ]
