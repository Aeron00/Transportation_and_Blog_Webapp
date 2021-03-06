# Generated by Django 4.0.2 on 2022-05-11 09:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=122)),
                ('desc', models.TextField()),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pro_Img', models.FileField(upload_to='Profile/')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=50)),
                ('Phone', models.IntegerField()),
                ('Address', models.CharField(max_length=200)),
                ('Date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('Date', models.DateField(default=datetime.date.today)),
                ('U_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ALL_FOR_ONE.signup')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File', models.FileField(upload_to='Blog/')),
                ('Title', models.CharField(max_length=30)),
                ('Detail', models.CharField(max_length=10000)),
                ('Date', models.DateField(default=datetime.date.today)),
                ('U_Name', models.CharField(max_length=50)),
                ('U_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ALL_FOR_ONE.signup')),
            ],
        ),
    ]
