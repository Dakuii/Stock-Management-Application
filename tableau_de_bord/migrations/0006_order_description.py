# Generated by Django 5.0.3 on 2024-07-09 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableau_de_bord', '0005_alter_product_options_product_brand_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
