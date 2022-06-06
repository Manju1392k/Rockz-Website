# Generated by Django 4.0.4 on 2022-06-06 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RocketBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rocket_Name', models.CharField(max_length=150)),
                ('Rocket_LaunchDate', models.DateField(max_length=10)),
                ('Rocket_LandingDate', models.DateField(max_length=10)),
                ('Rocket_Image', models.ImageField(upload_to='photos')),
                ('Rocket_Time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]