# Generated by Django 5.0.1 on 2024-01-15 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0002_blog_category_blogcat_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_category',
            name='blogcat_description',
            field=models.CharField(max_length=300),
        ),
    ]
