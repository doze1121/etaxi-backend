# Generated by Django 4.2.7 on 2023-11-10 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0002_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=200)),
                ('comment_person', models.CharField(max_length=500)),
                ('photo_person', models.ImageField(upload_to='')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pers', to='backend_api.city')),
            ],
        ),
    ]
