from django.db import models

# Create your models here.

class Sector(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Stock(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True)
    market_cap = models.FloatField()
    price = models.FloatField()
    pe_ratio = models.FloatField(null=True, blank=True)
    roe = models.FloatField(null=True, blank=True)
    roce = models.FloatField(null=True, blank=True)
    debt_to_equity = models.FloatField(null=True, blank=True)
    high_52 = models.FloatField(null=True, blank=True)
    low_52 = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.symbol} - {self.name}"
