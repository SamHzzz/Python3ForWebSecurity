import requests 
from bs4 import BeautifulSoup
import sys
import json


def check_url(raw_url):
    return raw_url.rstrip('/')

def get_csrf_token(url, session):

    response = session.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find("input", {"name": "csrf"})

        if result:
            print("CSRF Token : " + result["value"])
            return result["value"]
        else:
            print("[!] CSRF token not found!")
            sys.exit(1)            
    
    else:
        print("web request error.")
        sys.exit(1)


session = requests.Session()
args = sys.argv[1:]

try:
    raw_url = args[0]
    base_url = check_url(raw_url)
    login_url = base_url + '/login'
    get_csrf_token(login_url,session)
except:
    print("[!] Error\nUsage: python3 poc.py <lab_url>")

