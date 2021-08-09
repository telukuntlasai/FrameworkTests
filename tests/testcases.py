from apiClass import apiClass
import json
import requests
import pytest


def test_testcase1():
    str_symbol = 'IBM'
    apicl=apiClass()
    resp = apicl.fetchResponse(str_symbol=str_symbol)

    if resp.status_code == 200:
        if json.loads(resp.text)['Meta Data']['2. Symbol']==str_symbol:
            assert True
    else:
        assert False



def test_testcase2():
    str_symbol = 'IBM'
    resp = apiClass().fetchResponse(str_symbol=str_symbol,str_outputsize='compact')
    if resp.status_code == 200:
       if len(json.loads(resp.text)['Time Series (Daily)']) ==100 :
            assert True

    else:
        assert False



def test_testcase3():
    str_symbol = 'IBM'
    resp = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+str_symbol)
    errormessage='the parameter apikey is invalid or missing. Please claim your free API key on (https://www.alphavantage.co/support/#api-key). It should take less than 20 seconds.'
    if resp.status_code == 200:
       if json.loads(resp.text)['Error Message'] ==errormessage :
            assert True

    else:
        assert False

def test_testcase4():
    str_symbol = 'IBM'
    resp = apiClass().fetchResponse(str_symbol=str_symbol,str_outputsize='full')
    if resp.status_code == 200:
       if len(json.loads(resp.text)['Time Series (Daily)']) >100 :
            assert True

    else:
        assert False

def test_testcase5():
    str_symbol = 'IBM'
    apic=apiClass()
    resp = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey='+apic.apikey)
    errormessage='Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_DAILY.'
    if resp.status_code == 200:
       if json.loads(resp.text)['Error Message'] ==errormessage :
            assert True

    else:
        assert False