# Generated by Django 4.2.7 on 2024-01-29 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0006_watchpart_remove_orderitem_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchpart',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
