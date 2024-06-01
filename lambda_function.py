#source : https://www.youtube.com/watch?v=DLqB6ly5k0I

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

Charting_url ='https://chartink.com/screener/process'

Condition = {'scan_clause' : '( {57960} ( latest {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} < 0 and latest {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} < 0 and latest {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} > latest {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} and 1 day ago  {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} <= 1 day ago  {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} ) ) '}

with requests.session() as s:
    r_data = s.get(Charting_url)
    soup = bs(r_data.content, "lxml")
    meta = soup.find("meta",{"name" : "csrf-token"})["content"]
    
    header = {"X-Csrf-Token" : meta}

    data = s.post(Charting_url, headers=header, data=Condition).json()
    stock_list = pd.DataFrame(data["data"])
    print (stock_list)
    telegram_output = stock_list
    

# Sending Stock list to python 

TOKEN='7449783431:AAHqe61k6R14Z_YismA2VEJYeXsACZbpgYg'
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
#test_chat_id="-4287405834"
chat_id = "-1002199303920"
strategy_name = "TSI >= 0 Screener"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={strategy_name}"
message = telegram_output
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json())