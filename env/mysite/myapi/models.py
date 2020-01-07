from django.db import models

# Create your models here.
class Pegawai(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Barang(models.Model):
    pegawai = models.ForeignKey(Pegawai,on_delete=models.CASCADE,related_name='barangs',)
    nama_barang = models.CharField(max_length=60)
    harga_barang = models.CharField(max_length=60)
    def __str__(self):
        return self.pegawai.name
    