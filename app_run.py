import pandas as pd

def currencyExchangeRate():
    url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'
    table = pd.read_html(url)
    currency = pd.DataFrame(table[0])
    currency = currency.iloc[:,0:5] #iloc[a,b] -> a:index, b:columns 
    currency.columns = [u'幣別', u'現金匯率-本行買入', u'現金匯率-本行賣出', u'即期匯率-本行買入', u'即期匯率-本行賣出']    #rename columns, add u to save unicode
    currency[u'幣別'] = currency[u'幣別'].str.extract('(\w+)')  #reg columns[u'幣別']
    currency.to_csv('test1.csv')    #export csv
currencyExchangeRate() # 台灣銀行牌告即期匯率


# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
# import numpy as np
# import lxml
# import lzma

# def financical_stament(year, season, type):

#     if type == '綜合損益彙總表':
#         url = 'https://mops.twse.com.tw/mops/web/ajax_t163sb04'
#     elif type == '資產負債彙總表':
#         url = 'https://mops.twse.com.tw/mops/web/ajax_t163sb05'
#     elif type == '營益分析彙總表':
#         url = 'https://mops.twse.com.tw/mops/web/ajax_t163sb06'
#     else:
#         print('type does not match')

#     r = requests.post(url, {
#         'encodeURIComponent':1,
#         'step':1,
#         'firstin':1,
#         'off':1,
#         'TYPEK':'sii',
#         'year':str(year),
#         'season':str(season),
#     })

#     r.encoding = 'utf8'
#     dfs = pd.read_html(r.text, header=None)
#     return pd.concat(dfs[1:], axis=0, sort=False)\
#              .set_index(['公司代號'])\
#              .apply(lambda s: pd.to_numeric(s, errors='raise'))


# financical_stament(108,1,'綜合損益彙總表')
# # # 綜合損益彙總表
# # # 資產負債彙總表
# # # 營益分析彙總表
