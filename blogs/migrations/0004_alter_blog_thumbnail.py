# Generated by Django 4.2.2 on 2023-06-12 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_blog_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='media'),
        ),
    ]
