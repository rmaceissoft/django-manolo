# Generated by Django 3.1.4 on 2020-12-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0022_auto_20201212_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='updated_institutions',
            field=models.JSONField(blank=True, null=True),
        ),
    ]