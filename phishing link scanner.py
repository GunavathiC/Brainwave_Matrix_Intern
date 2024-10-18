import requests
from urllib.parse import urlparse

def scan_url(url):

    try:
        requests.head(url)
    except requests.exceptions.RequestException:
        print("Invalid URL!")
        return

    suspicious_keywords = ["login", "password", "update", "verify"]
    for keyword in suspicious_keywords:
        if keyword in url.lower():
            print("Potential phishing link detected!!!")
            return

    parsed_url = urlparse(url)
    if parsed_url.netloc != parsed_url.netloc.split('.')[-2] + '.' + parsed_url.netloc.split('.')[-1]:
        print("Potential phishing link detected!!!")
        return

    print("Link appears legitimate.")

url = input("Enter URL to scan: ")
scan_url(url)

