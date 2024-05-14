import requests 
from bs4 import BeautifulSoup
import sys
import json

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
