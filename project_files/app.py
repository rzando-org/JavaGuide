```python
import os
import subprocess

def fetch_data():
    url = input("Enter URL: ")
    result = subprocess.run(['curl', '-s', url], capture_output=True, text=True)
    print(result.stdout)

fetch_data()
```