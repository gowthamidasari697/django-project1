# Generated by Django 5.0.1 on 2024-01-16 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0003_alter_blog_category_blogcat_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_email', models.EmailField(max_length=254)),
                ('u_message', models.CharField(max_length=200)),
            ],
        ),
    ]
