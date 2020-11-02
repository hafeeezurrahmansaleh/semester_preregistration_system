# Generated by Django 2.1.7 on 2020-10-10 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tID', models.CharField(max_length=30, unique=True)),
                ('tName', models.CharField(max_length=30)),
                ('tInitial', models.CharField(max_length=10, unique=True)),
                ('tDesignation', models.CharField(max_length=20)),
                ('tPhone', models.CharField(max_length=20)),
                ('tEmail', models.CharField(max_length=40)),
            ],
        ),
    ]
