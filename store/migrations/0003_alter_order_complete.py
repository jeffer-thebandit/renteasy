# Generated by Django 3.2.9 on 2021-11-27 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
