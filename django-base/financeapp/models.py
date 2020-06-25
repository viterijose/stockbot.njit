from django.db import models

# Create your models here.
class InvestorUser(models.Model):
    FirstName=models.CharField(max_length=15)
    LastName=models.CharField(max_length=15)
    UserEmail=models.EmailField(max_length=35)
    InvestorType=models.TextChoices('type','STOCKS OPTIONS FUTURES FOREX')
    Username=models.CharField(max_length=20)

class Stock(models.Model):
    TickerSymbol=models.CharField(max_length=6)
    CompanyName=models.CharField(max_length=40,default="Company Name")
    LastPrice=models.DecimalField(decimal_places=3,max_digits=10)
    PercentChange=models.DecimalField(decimal_places=3,max_digits=6,default="2")
    PriceChange=models.DecimalField(decimal_places=3,max_digits=8,default="2.50")
    EarningsDate=models.DateField(auto_now=True)
    TodayDate=models.DateTimeField(auto_now=True)
    CompanyDesc=models.TextField(default="Company Description")
    StockSector=models.CharField(max_length=8,choices=[
        ('TCH','Tech'),
        ('TO','Tourism'),
        ('ENGY','ENERGY'),
        ('HTL','Healthcare'),
        ('FNC','Financials'),
        ('RTN','Restaurant'),
        ('RTL','Retail'),
        ('AVG','MarketAVG')
    ],default="None")