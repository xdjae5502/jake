# Generated by Django 4.2.7 on 2024-01-29 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0007_watchpart_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchpart',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='watch_parts/'),
        ),
    ]
