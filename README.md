SecureCrypt

Modern and secure file encryption application built with Python.

SecureCrypt allows users to encrypt any file with a password and safely share it with others.
Only users with the correct password can decrypt and access the original file.

Features
AES-based secure encryption using Fernet
Password protected file access
Modern GUI interface
Encrypted .crypt file format
Original filename recovery
Strong PBKDF2 password hashing
Wrong password protection
Easy file sharing
Lightweight single-file application
Screenshots

Add your application screenshots here.

assets/screenshot.png
Installation

Clone the repository:

git clone https://github.com/TurkerAlbayrak/python-file-crypt-desktop-app.git
cd securecrypt

Install dependencies:

pip install cryptography

Run the application:

python app.py
How It Works
Encryption
Select a file
Enter a password
File gets encrypted
New .crypt file is generated
Decryption
Open .crypt file
Enter correct password
Original file is restored
Security

SecureCrypt uses:

PBKDF2HMAC (SHA256)
Random Salt Generation
Fernet Symmetric Encryption
Password-Based Key Derivation

Passwords are never stored.

Project Structure
securecrypt/
│
├── app.py
├── README.md
├── requirements.txt
└── assets/
Example

Original file:

photo.png

Encrypted file:

photo.png.crypt

Even if the file extension changes, the encrypted content remains protected.

Future Features

Drag & Drop support
Multi-file encryption
Dark mode improvements
File expiration system
QR password sharing
LAN secure transfer
EXE build for Windows
Technologies Used
Python
Tkinter
Cryptography

Author

Developed by Turker.
