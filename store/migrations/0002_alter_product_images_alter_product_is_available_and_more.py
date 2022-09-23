# Generated by Django 4.0 on 2022-07-21 10:47

import computed_property.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(upload_to='photos/products', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='Disponible'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=computed_property.fields.ComputedIntegerField(compute_from='stock_total', default=1, editable=False, verbose_name='Stock'),
            preserve_default=False,
        ),
    ]
