# Generated by Django 3.1.7 on 2021-03-22 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['title', '-id']},
        ),
    ]
