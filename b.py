import json
import urllib
url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
parameters = {'ip': '90.156.201.27', 'apikey': '--APIKEY--'}
response = urllib.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
#print response
response_dict = json.loads(response)
