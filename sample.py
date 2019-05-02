"""
Fetch title, current price, and currency name for all eBay items with UPC
753759077600, using HTTP GET.

Author: David Joel Lambert
Date: November 1, 2017

Written for Python 2.7
"""

# IMPORTS

import urllib2
import collections
import xml.etree.ElementTree as eTree

# BUILD URL

urlRoot = 'http://svcs.ebay.com/services/search/FindingService/v1'
upc     = '753759077600'

myHeaders1 = collections.OrderedDict()
myHeaders1['OPERATION-NAME'                ] = 'findItemsByProduct'
myHeaders1['SERVICE-VERSION'               ] = '1.30.0'
myHeaders1['SECURITY-APPNAME'              ] = 'DavidLam-DavidLam-PRD-551ca6568-b3aa9a5b'
myHeaders1['RESPONSE-DATA-FORMAT'          ] = 'XML'
myHeaders1['SERVICE-NAME'                  ] = 'FindingService'
myHeaders1['GLOBAL-ID'                     ] = 'EBAY-US'

myHeaders2 = collections.OrderedDict()
myHeaders2['productId.@type'               ] = 'UPC'
myHeaders2['productId'                     ] = upc
myHeaders2['paginationInput.entriesPerPage'] = '1000'

headerList1 = [(key + '=' + value) for key, value in myHeaders1.items()]
middle      = ['REST-PAYLOAD', ]
headerList2 = [(key + "=" + value) for key, value in myHeaders2.items()]

url = urlRoot + '?' + '&'.join(headerList1 + middle + headerList2)

# BUILD HEAD

# No Head

# BUILD BODY

# No Body

# GO

r = urllib2.Request(url)
u = urllib2.urlopen(r)
response = u.read()

root = eTree.fromstring(response)
loc = 1 + root.tag.find("}")
xmlns = root.tag[:loc]
pretty = 'The item with title "%s" is currently priced %.2f in %s.'
divider = 64*"="

print(divider)
print("The Title and Price Of All Items For Sale With UPC %s." % upc)
print(divider)

list2 = root.findall(xmlns + "searchResult")
for item2 in list2:
    list3 = item2.findall(xmlns + "item")
    for item3 in list3:
        list4_1 = item3.findall(xmlns + "title")
        for item4_1 in list4_1:
            title = item4_1.text
        list4_2 = item3.findall(xmlns + "sellingStatus")
        for item5 in list4_2:
            list6 = item5.findall(xmlns + "currentPrice")
            for item6 in list6:
                currentPrice = float(item6.text)
                currencyId = item6.get("currencyId")
                print(pretty % (title, currentPrice, currencyId))

print(divider)
