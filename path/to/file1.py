```python
import os

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

data = read_file('sensitive_data.txt')
print(data)
```