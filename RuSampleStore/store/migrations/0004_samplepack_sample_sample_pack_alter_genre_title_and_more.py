# Generated by Django 4.1.6 on 2023-02-12 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_sample_artist_remove_sample_instrument_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SamplePack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cover_src', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='sample',
            name='sample_pack',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.sample'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sample',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
