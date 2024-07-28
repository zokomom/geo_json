import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break
        
    url =  serviceurl + urllib.parse.urlencode(   
    {'address': address, 'key': 42})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:  
        js=json.loads(data)
    except:
        js=None
        
    print(json.dumps(js, indent=4))
    
    if js and 'results' in js:
        place_id = js['results'][0]['place_id']
        print('Place ID: ', place_id)
    else:
        print('No place ID found')

