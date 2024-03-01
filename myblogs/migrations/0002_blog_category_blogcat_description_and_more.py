# Generated by Django 5.0.1 on 2024-01-15 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_category',
            name='blogcat_description',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog_category',
            name='blogcat_img',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
