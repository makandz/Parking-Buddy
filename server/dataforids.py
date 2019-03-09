import json
from pprint import pprint
import math

#radius of the earth
R = 6373.0

def calc(a, b):
    #location of the user
    lng1 = a
    lt1 = b

    def distance(origin, destination):
        lat1, lon1 = origin
        lat2, lon2 = destination
        radius = 6371 # km

        dlat = math.radians(lat2-lat1)
        dlon = math.radians(lon2-lon1)
        a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = radius * c

        return d

    with open('data.json') as f:
        data = json.load(f)

    values = []

    for i in data['carparks']:
        dist = distance((lt1, lng1), (float(i['lat']), float(i['lng'])))
        if (dist < 1):
            values.append([dist, i['lat'], i['lng'], i['address']])

    values.sort()
    f.close()
    return values

from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def send_my_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        response = BytesIO()
        body = body.decode("utf-8").split(",")
        vals = calc(float(body[0]), float(body[1]))
        response.write(b"{ \"results\": {")
        for i in range(len(vals)):
            response.write(b'[')
            response.write(("'" + str(vals[i][0]) + "'").encode("utf-8"))
            response.write(b",")
            response.write(("'" + str(vals[i][1]) + "'").encode("utf-8"))
            response.write(b",")
            response.write(("'" + str(vals[i][2]) + "'").encode("utf-8"))
            response.write(b",")
            response.write(("'" + str(vals[i][3]) + "'").encode("utf-8"))
            if i != len(vals) - 1:
                response.write(b"],")
            else:
                response.write(b']')
        response.write(b"} }")
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')  
        self.end_headers()
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()