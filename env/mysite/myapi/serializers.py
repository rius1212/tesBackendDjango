from rest_framework import serializers

from .models import Pegawai,Barang


class BarangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barang
        fields = ('pegawai','nama_barang','harga_barang')

class PegawaiSerializer(serializers.ModelSerializer):
    barangs = BarangSerializer(many=True, read_only=True)
    class Meta:
        model = Pegawai
        fields = ('id','name', 'alias','barangs')