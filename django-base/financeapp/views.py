from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Stock
import requests

from bs4 import BeautifulSoup



def index(request):
    return render(request, 'financeapp/home.html')


def gainers(request):
    stocks = Stock.objects.all()
    context = {'stocks': stocks}
    return render(request, 'financeapp/gainers.html',context)


def losers(request):
    stocks = Stock.objects.all()
    context = {'stocks': stocks}
    return render(request, 'financeapp/losers.html',context)

    
def pennystocks(request):
    stocks = Stock.objects.all()
    context = {'stocks': stocks}
    return render(request, 'financeapp/pennystocks.html',context)

def techstocks(request):
    stocks = Stock.objects.all()
    context = {'stocks': stocks}
    return render(request, 'financeapp/techstocks.html',context)

def overall(request):
    stocks = Stock.objects.all()
    context = {'stocks': stocks}
    return render(request, 'financeapp/overall.html',context)

def homes(request):
    # while True:
    response = requests.get(f"https://finance.yahoo.com/gainers")

    # beautiful soup
    soup = BeautifulSoup(response.text, 'html.parser')
    stocks_ticker = []
    # print(f"{soup}")
    for result in soup.select('a'):
        ticker_symbol = str(result.string)
        stocks_ticker.append(ticker_symbol)
    stocks_ticker.remove("All Screeners")
    stocks_ticker.remove("Yahoo")
    # stocks_ticker.remove(str("None"))
    # list(filter(None, stocks_ticker))
    print(f"{stocks_ticker[18:118]}")
    res = {'restock':stocks_ticker[18:118]}
        # print(res)
    return render(request, 'financeapp/homes.html', res)