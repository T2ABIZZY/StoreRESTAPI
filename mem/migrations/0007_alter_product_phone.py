# Generated by Django 4.0.3 on 2022-03-28 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mem', '0006_alter_product_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='phone',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True),
        ),
    ]
