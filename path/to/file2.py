```python
import subprocess

def execute_command(cmd):
    result = subprocess.run(cmd, shell=True)
    return result.stdout

output = execute_command('ls -l')
print(output)
```