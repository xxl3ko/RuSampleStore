# Generated by Django 4.1.6 on 2023-02-13 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_sample_sample_pack'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='oleg',
        ),
    ]
