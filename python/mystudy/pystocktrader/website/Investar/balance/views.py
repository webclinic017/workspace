from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

def get_data(symbol):
    url = 'http://finance.naver.com/item/sise.nhn?code={}'.format(symbol)

    # 해당 사이트는 반드시 헤더 정보를 요구하기 때문에 헤더를 넘겨줘야 함
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}

    req = requests.get(url, headers=headers)

    html = BeautifulSoup(req.text, 'html.parser')
    cur_price = html.find('strong', id='_nowVal')
    cur_rate = html.find('strong', id='_rate')
    stock = html.find('title')
    stock_name = stock.text.split(':')[0].strip()
    return cur_price.text, cur_rate.text.strip(), stock_name

    # with urlopen(url, headers=headers) as doc:
    #     soup = BeautifulSoup(doc, 'lxml', from_encoding='euc-kr')
    #     cur_price = soup.find('strong', id='_nowval')
    #     cur_rate = soup.find('strong', id='_rate')
    #     stock = soup.find('title')
    #     sotck_name = stock.text.split(':')[0].strip()
    #     return cur_price.text, cur_rate.text.strip(), sotck_name

def main_view(request):
    querydict = request.GET.copy()
    mylist = querydict.lists()
    rows = []
    total = 0

    for x in mylist:
        cur_price, cur_rate, stock_name = get_data(x[0])
        price = cur_price.replace(',', '')
        stock_count = format(int(x[1][0]), ',')
        sum = int(price) * int(x[1][0])
        stock_sum = format(sum, ',')
        rows.append([stock_name, x[0], cur_price, stock_count, cur_rate, stock_sum])
        total = total + int(price) * int(x[1][0])

    total_amount = format(total, ',')
    values = {'rows' : rows, 'total' : total_amount}
    return render(request, 'balance.html', values)