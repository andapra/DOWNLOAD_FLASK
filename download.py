import urllib3

http = urllib3.PoolManager()
http.request('https://localhost:5000/download/export.csv')