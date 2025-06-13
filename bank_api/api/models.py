from django.db import models

class Bank(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'banks'
    def __str__(self):
        return self.name
    
class Branch(models.Model):
    ifsc = models.CharField(max_length=11, primary_key=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'branches'
    def __str__(self):
        return f'{self.ifsc} - {self.branch}'