# Generated by Django 4.2.1 on 2023-05-21 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KGTravelGuide', '0002_attachment_delete_author_alter_place_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
