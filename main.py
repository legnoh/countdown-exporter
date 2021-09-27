import time
import os
from datetime import datetime, timedelta
from prometheus_client import CollectorRegistry, Gauge, start_http_server

if __name__ == '__main__':
    registry = CollectorRegistry()
    start_http_server(int(os.environ['PORT']), registry=registry)

    g = Gauge('countdown_until_seconds','', ['date'], registry=registry)

    until_date = int(os.environ['UNTIL_DATE'])
    
    while True:
        now = int(time.time())
        today = datetime.today()
        for date in range(until_date):
            day_timestamp = int(today.timestamp())
            until_seconds = day_timestamp - now
            until_label = datetime.strftime(today, '%Y-%m-%d')
            g.labels(until_label).set(until_seconds)
            today = today + timedelta(days=1)
        time.sleep(600)
