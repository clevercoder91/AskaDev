# Generated by Django 2.2.6 on 2020-08-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0012_liker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='url',
            field=models.CharField(default='55bad9a9fbd2c71a2ffba10568e60a329b9b14c3', max_length=32),
        ),
    ]
