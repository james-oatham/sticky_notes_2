# Generated by Django 5.0.6 on 2024-06-11 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sticky_notes_2_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour_name', models.CharField(max_length=255)),
            ],
        ),
    ]
