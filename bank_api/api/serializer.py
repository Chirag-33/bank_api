from rest_framework import serializers
from . models import Bank,Branch

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Bank
        fields = '__all__'
    
class BranchSerializer(serializers.ModelSerializer):
    bank =BankSerializer(read_only = True)
    class Meta:
        model = Branch
        fields = '__all__'