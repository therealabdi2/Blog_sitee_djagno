# Generated by Django 3.2.4 on 2021-07-07 18:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0002_auto_20210701_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
            ],
        ),
    ]
