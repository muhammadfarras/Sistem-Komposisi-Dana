# Generated by Django 3.2.9 on 2021-11-29 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SistemInformasiKeuangan', '0006_auto_20211125_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account3632',
            name='reference_number',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='account3633',
            name='reference_number',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='account3635',
            name='reference_number',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='account3639',
            name='reference_number',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='account38105',
            name='reference_number',
            field=models.CharField(max_length=200),
        ),
    ]
