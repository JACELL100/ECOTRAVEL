# Generated by Django 5.1.4 on 2024-12-12 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco_travel_app', '0005_remove_profile_travel_miles_saved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='preferences',
            field=models.CharField(max_length=200),
        ),
    ]
