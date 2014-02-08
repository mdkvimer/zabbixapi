#!/usr/bin/env python
#coding=utf-8
import json
import urllib2
# based url and required header
url = "http://10.131.10.73/zabbix/api_jsonrpc.php"
header = {"Content-Type": "application/json"}
# request json
data = json.dumps(
{
    "jsonrpc":"2.0",
    "method":"event.get",
    "params":{
        "output": "extend",
        "select_acknowledges": "extend",
        "sortfield": ["clock", "eventid"],
        "sortorder": "DESC"
    },
    "auth":"d2290099d27f4ad25026cec70db1b834", # the auth id is what auth script returns, remeber it is string
    "id":1,
})
# create request object
request = urllib2.Request(url,data)
for key in header:
    request.add_header(key,header[key])
#get event data
try:
    result = urllib2.urlopen(request)
except IOError, e:
    if hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
    elif hasattr(e, 'code'):
        print 'The server could not fulfill the request.'
        print 'Error code: ', e.code
else:
    response = json.loads(result.read())
    result.close()
    for i in response["result"]:
        print i.keys()