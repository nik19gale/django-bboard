# Generated by Django 4.0.3 on 2023-01-07 18:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('desc', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=300)),
                ('text', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(limit_value=0.01)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='ads.category')),
            ],
            options={
                'verbose_name': 'Advertisement',
                'verbose_name_plural': 'Advertisements',
            },
        ),
    ]
