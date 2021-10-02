import subprocess

def add(path):
    res = subprocess.run(['ipfs', 'add', '-Q', path], capture_output=True)
    return str(res.stdout.strip())

link = add('data-wikimedia-en_es.argosdata')

print(link)
