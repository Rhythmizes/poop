import threading
import requests
import time

def send_data(url):
    data = b'\x010000000000' * (1024*1024*81)
    r = requests.post(url, data=data)

if __name__ == '__main__':
    urls = ['https://enn2idgnmxxse.x.pipedream.net/']
    for url in urls:
        for i in range(100):
            t = threading.Thread(target=send_data, args=(url,))
            t.start()
            time.sleep(1)