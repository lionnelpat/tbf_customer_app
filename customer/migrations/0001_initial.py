# Generated by Django 3.2.5 on 2023-06-09 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('photo', models.ImageField(default='category_default.png', upload_to='category')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_ref', models.CharField(max_length=10, unique=True)),
                ('lastname', models.CharField(max_length=30)),
                ('firstname', models.CharField(blank=True, max_length=30, null=True)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('customer_type', models.CharField(choices=[('A', 'AZURE'), ('P', 'PLATINIUM'), ('G', 'GOLD')], max_length=1)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='customers_images')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_ref', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('qty_in_stock', models.IntegerField()),
            ],
        ),
    ]
