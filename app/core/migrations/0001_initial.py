# Generated by Django 4.0.4 on 2022-11-09 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('avatar', models.FileField(max_length=255, null=True, upload_to='media/images')),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=32)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
            ],
        ),
    ]
