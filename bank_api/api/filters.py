import django_filters
from .models import Branch

class BranchFilter(django_filters.FilterSet):
    class Meta:
        model = Branch
        fields = {
            'bank__name':['exact', 'icontains'],
            'city':['exact','icontains']
        }