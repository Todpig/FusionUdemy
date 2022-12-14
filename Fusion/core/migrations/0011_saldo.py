# Generated by Django 4.1.1 on 2022-10-21 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_produtos_saldo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saldo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('saldo', models.IntegerField(null=True, verbose_name='Saldo')),
            ],
            options={
                'verbose_name': 'Saldo',
                'verbose_name_plural': 'Saldos',
            },
        ),
    ]
