# Generated by Django 2.1.7 on 2019-03-17 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGFan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sgmovies',
            name='description',
            field=models.CharField(max_length=5000),
        ),
    ]
