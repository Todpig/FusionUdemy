# Generated by Django 4.1.1 on 2022-10-21 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_delete_saldo'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='saldo',
            field=models.IntegerField(null=True, verbose_name='Saldo'),
        ),
    ]
