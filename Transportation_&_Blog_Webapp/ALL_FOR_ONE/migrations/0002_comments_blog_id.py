# Generated by Django 4.0.2 on 2022-05-11 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ALL_FOR_ONE', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='Blog_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ALL_FOR_ONE.blog'),
            preserve_default=False,
        ),
    ]
