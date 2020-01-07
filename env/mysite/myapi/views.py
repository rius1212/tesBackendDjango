from rest_framework import viewsets

from .serializers import PegawaiSerializer,BarangSerializer
from .models import Pegawai,Barang


class PegawaiViewSet(viewsets.ModelViewSet):
    queryset = Pegawai.objects.all().order_by('name')
    serializer_class = PegawaiSerializer

class BarangViewSet(viewsets.ModelViewSet):
    queryset = Barang.objects.all().order_by('nama_barang')
    serializer_class = BarangSerializer