# Generated by Django 4.2.7 on 2023-12-11 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMaster',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_price', models.IntegerField(max_length=10)),
                ('product_image', models.ImageField(upload_to='product_images/')),
                ('product_model', models.CharField(max_length=50)),
                ('product_ram', models.CharField(max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.productmaster')),
            ],
        ),
    ]
