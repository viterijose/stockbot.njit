from django.contrib import admin

# Register your models here.
from .models import InvestorUser
from .models import Stock

admin.site.register(InvestorUser)
admin.site.register(Stock)
