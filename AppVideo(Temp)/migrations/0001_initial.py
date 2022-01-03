# Generated by Django 3.2 on 2021-12-25 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='streamVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Video title')),
                ('slug', models.SlugField(max_length=264, unique=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_uploader', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liker_user', to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_video', to='AppVideo.streamvideo')),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_comment', to='AppVideo.streamvideo')),
            ],
        ),
    ]