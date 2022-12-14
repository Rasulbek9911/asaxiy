# Generated by Django 3.2.7 on 2022-07-31 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20220731_1852'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='sub_category',
            new_name='parent',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.category'),
        ),
    ]
