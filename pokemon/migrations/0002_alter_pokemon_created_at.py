# Generated by Django 4.0.4 on 2022-07-19 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]