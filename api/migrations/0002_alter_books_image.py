# Generated by Django 4.1.3 on 2022-11-09 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
