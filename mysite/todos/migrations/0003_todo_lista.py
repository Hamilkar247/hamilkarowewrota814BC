# Generated by Django 3.1 on 2020-09-03 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_todolistitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='lista',
            field=models.CharField(default='lista', help_text='This field is required', max_length=100),
        ),
    ]
