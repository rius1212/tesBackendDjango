# Generated by Django 2.2 on 2020-01-07 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_barang_harga_barang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='pegawai',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barangs', to='myapi.Pegawai'),
        ),
    ]
