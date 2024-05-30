# Generated by Django 5.0.4 on 2024-05-30 20:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField(default=0)),
                ('duration', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=100)),
                ('experience', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13)),
                ('parents_phone', models.CharField(max_length=13)),
                ('telegram', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.course')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.teacher')),
            ],
        ),
    ]
