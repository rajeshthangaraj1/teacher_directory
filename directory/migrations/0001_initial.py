# Generated by Django 3.2.5 on 2021-07-31 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=150)),
                ('lastname', models.CharField(max_length=150)),
                ('profileimg', models.ImageField(upload_to='profile')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('phone', models.CharField(max_length=150)),
                ('room_number', models.CharField(max_length=50)),
                ('subjects', models.CharField(max_length=50)),
            ],
        ),
    ]