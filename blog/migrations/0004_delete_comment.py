# Generated by Django 3.2.4 on 2021-07-07 18:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
