# Generated by Django 3.2.8 on 2021-10-31 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0004_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Description',
            field=models.CharField(max_length=900, null=True),
        ),
    ]
