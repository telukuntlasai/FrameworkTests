from apiClass import apiClass
from unittest import TestCase
import json

class test_testcase():
    def test_fetch_response(self):
        resp=apiClass().fetchResponse(str_symbol='IBM')
        if resp.status_code == 200 :
            assert True


        else:
            assert False




