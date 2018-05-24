#-*- coding: utf-8 -*-

import urllib.request

def query_sender():

    url = 'http://apis.data.go.kr/1192000/openapi/service/ManageAcst0400Service/getAcst0400List?'
    #접속 URL?로구분같음
    key = 'serviceKey=%2BMsP4iAokY9ZDh3HACym%2FxTgvDJCmNb8W4yvsB3%2FJk95ewAW6HE0uA95FK4yKOXNvPoKQ8EdWiG1kZjXXtC1kg%3D%3D'
    #나의 인증키
    requestParameter = '&numOfRows=10&pageSize=10&pageNo=10&startPage=10&baseDt=20131003&fromDt=20131001&toDt=20131003'


    request = urllib.request.Request(url + key + requestParameter)
    request.get_method = lambda: 'GET'
    response_body = urllib.request.urlopen(request).read()
    u = str(response_body, "utf-8")
    return u

s = query_sender()

print(s)
