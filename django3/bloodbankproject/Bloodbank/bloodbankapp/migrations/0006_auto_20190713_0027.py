# Generated by Django 2.2.2 on 2019-07-12 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbankapp', '0005_auto_20190713_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donors',
            name='blood_group',
            field=models.CharField(max_length=30),
        ),
    ]
