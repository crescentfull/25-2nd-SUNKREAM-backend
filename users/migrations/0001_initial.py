# Generated by Django 3.2.8 on 2021-10-19 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('eamil', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=20, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('point', models.PositiveIntegerField(default=1000000)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
