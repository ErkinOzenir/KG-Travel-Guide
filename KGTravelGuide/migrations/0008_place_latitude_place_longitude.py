# Generated by Django 4.2.1 on 2023-05-29 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KGTravelGuide', '0007_alter_attachment_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='latitude',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='longitude',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]
