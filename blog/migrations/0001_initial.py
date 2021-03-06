# Generated by Django 3.2.4 on 2021-07-01 13:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('excerpt', models.CharField(max_length=250)),
                ('image_name', models.URLField(blank=True)),
                ('date', models.DateField()),
                ('slug', models.SlugField(blank=True, default='')),
                ('content', models.CharField(max_length=1000)),
                ('author',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts',
                                   to='blog.author')),
                ('tags', models.ManyToManyField(to='blog.PostTag')),
            ],
        ),
    ]
