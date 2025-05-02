```python
import json

def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

config = load_json('config.json')
print(config)
```