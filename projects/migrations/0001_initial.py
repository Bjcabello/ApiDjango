# Generated by Django 5.0.2 on 2024-04-18 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=50)),
                ('technology', models.TextField(max_length=200)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
