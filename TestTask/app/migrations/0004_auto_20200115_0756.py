# Generated by Django 2.2 on 2020-01-15 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('books', 'Books'), ('movies', 'Movies')], max_length=255),
        ),
    ]