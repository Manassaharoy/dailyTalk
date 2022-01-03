# Generated by Django 3.2 on 2021-12-30 03:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppVideo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-comment_date']},
        ),
        migrations.AlterModelOptions(
            name='streamvideo',
            options={'ordering': ['-upload_date']},
        ),
        migrations.AddField(
            model_name='streamvideo',
            name='videoURL',
            field=models.CharField(default=django.utils.timezone.now, max_length=550, verbose_name='Video url'),
            preserve_default=False,
        ),
    ]
