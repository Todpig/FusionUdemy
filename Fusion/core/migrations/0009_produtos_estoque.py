# Generated by Django 4.1.1 on 2022-10-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_produtos_delete_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='estoque',
            field=models.CharField(max_length=10, null=True, verbose_name='Estoque'),
        ),
    ]