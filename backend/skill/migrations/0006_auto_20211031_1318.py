# Generated by Django 3.2.8 on 2021-10-31 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0005_alter_details_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='Slug',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='Slug',
            field=models.CharField(max_length=200, null=True),
        ),
    ]