# Generated by Django 3.2.18 on 2023-03-21 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelsapp', '0002_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='img',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
