import requests
from datetime import datetime

def check_url(url):
    try:
        response = requests.get(url, timeout=5)
        return {
            "url": url,
            "status": response.status_code,
            "time": str(datetime.now())
        }
    except Exception as e:
        return {
            "url": url,
            "error": str(e),
            "time": str(datetime.now())
        }
    
    