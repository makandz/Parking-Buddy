import json
from pprint import pprint

with open('./server/data.json') as f:
    data = json.load(f)

for i in data['carparks']:
    print(i['lat'], i['lng'])