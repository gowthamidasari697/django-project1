# Generated by Django 5.0.1 on 2024-01-23 10:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0006_blog_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='blog_description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
