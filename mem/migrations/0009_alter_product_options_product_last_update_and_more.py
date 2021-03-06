# Generated by Django 4.0.3 on 2022-04-09 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mem', '0008_remove_product_last_update'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='product',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
