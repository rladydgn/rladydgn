# Generated by Django 4.0.3 on 2022-07-24 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=15, unique=True)),
                ('phone_number', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('salt', models.IntegerField(unique=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
        ),
    ]
