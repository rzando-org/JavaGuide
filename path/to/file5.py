```python
import sqlite3

def query_db(query):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

results = query_db('SELECT * FROM users')
print(results)
```