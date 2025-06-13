from django.shortcuts import render
from .models import Bank,Branch
from .serializer import BankSerializer,BranchSerializer
from rest_framework import viewsets
from .filters import BranchFilter
from django_filters.rest_framework import DjangoFilterBackend
class BankViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BranchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BranchFilter