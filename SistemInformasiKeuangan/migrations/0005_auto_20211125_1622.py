# Generated by Django 3.2.9 on 2021-11-25 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SistemInformasiKeuangan', '0004_auto_20211125_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account3632',
            name='code_sof',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.PROTECT, to='SistemInformasiKeuangan.vatype'),
        ),
        migrations.AlterField(
            model_name='account3633',
            name='code_sof',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.PROTECT, to='SistemInformasiKeuangan.vatype'),
        ),
        migrations.AlterField(
            model_name='account3635',
            name='code_sof',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.PROTECT, to='SistemInformasiKeuangan.vatype'),
        ),
        migrations.AlterField(
            model_name='account3639',
            name='code_sof',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.PROTECT, to='SistemInformasiKeuangan.vatype'),
        ),
        migrations.AlterField(
            model_name='account38105',
            name='code_sof',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.PROTECT, to='SistemInformasiKeuangan.vatype'),
        ),
    ]