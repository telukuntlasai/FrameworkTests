import requests
import pytest
import pytest_html

class apiClass:

    apikey = 'H5BDQ935F8R54REL'

    primaryurl = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey='


    def fetchResponse(self,str_symbol,str_outputsize=None,str_datatype=None):

        try:
            self.primaryurl = self.primaryurl+self.apikey+'&symbol='+str_symbol
            if str_outputsize is not  None:
                self.primaryurl=self.primaryurl+'&outputsize='+str_outputsize
            if str_datatype is not  None:
                self.primaryurl=self.primaryurl+'&datatype='+str_datatype

            response =requests.get(self.primaryurl)
            print(response)
            return response
        except Exception as e:
            print(str(e))