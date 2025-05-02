```python
class UserModel:
    def __init__(self, username):
        self.username = username
        self.is_admin = False

    def login(self, password):
        if password == "secret":
            self.is_admin = True
            return True
        else:
            return False
```