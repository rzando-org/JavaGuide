```python
import requests

def fetch_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text

data = fetch_url('http://example.com')
print(data)
```