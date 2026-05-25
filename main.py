import os
import json
import base64
import hashlib
from tkinter import *
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

# =========================
# KEY GENERATION
# =========================

def generate_key(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )

    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key


# =========================
# ENCRYPT FILE
# =========================

def encrypt_file(filepath, password):
    try:
        with open(filepath, "rb") as file:
            file_data = file.read()

        salt = os.urandom(16)
        key = generate_key(password, salt)
        fernet = Fernet(key)

        encrypted_data = fernet.encrypt(file_data)

        metadata = {
            "filename": os.path.basename(filepath),
            "salt": base64.b64encode(salt).decode()
        }

        final_data = {
            "metadata": metadata,
            "data": base64.b64encode(encrypted_data).decode()
        }

        output_file = filepath + ".crypt"

        with open(output_file, "w") as file:
            json.dump(final_data, file)

        messagebox.showinfo(
            "Success",
            f"File encrypted successfully!\n\nSaved as:\n{output_file}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# =========================
# DECRYPT FILE
# =========================

def decrypt_file(filepath, password):
    try:
        with open(filepath, "r") as file:
            content = json.load(file)

        metadata = content["metadata"]

        salt = base64.b64decode(metadata["salt"])
        encrypted_data = base64.b64decode(content["data"])

        key = generate_key(password, salt)
        fernet = Fernet(key)

        decrypted_data = fernet.decrypt(encrypted_data)

        original_filename = metadata["filename"]

        output_path = os.path.join(
            os.path.dirname(filepath),
            "DECRYPTED_" + original_filename
        )

        with open(output_path, "wb") as file:
            file.write(decrypted_data)

        messagebox.showinfo(
            "Success",
            f"File decrypted successfully!\n\nSaved as:\n{output_path}"
        )

    except Exception:
        messagebox.showerror(
            "Error",
            "Wrong password or corrupted file!"
        )


# =========================
# FILE PICKER
# =========================

selected_file = None

def choose_file():
    global selected_file

    filepath = filedialog.askopenfilename()

    if filepath:
        selected_file = filepath
        file_label.config(text=os.path.basename(filepath))


# =========================
# BUTTON ACTIONS
# =========================

def encrypt_action():
    if not selected_file:
        messagebox.showwarning("Warning", "Choose a file first!")
        return

    password = password_entry.get()

    if not password:
        messagebox.showwarning("Warning", "Enter password!")
        return

    encrypt_file(selected_file, password)


def decrypt_action():
    if not selected_file:
        messagebox.showwarning("Warning", "Choose a file first!")
        return

    password = password_entry.get()

    if not password:
        messagebox.showwarning("Warning", "Enter password!")
        return

    decrypt_file(selected_file, password)


# =========================
# GUI
# =========================

root = Tk()
root.title("SecureCrypt")
root.geometry("500x300")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

title = Label(
    root,
    text="SecureCrypt",
    font=("Arial", 24, "bold"),
    fg="white",
    bg="#1e1e1e"
)
title.pack(pady=20)

file_btn = Button(
    root,
    text="Choose File",
    command=choose_file,
    width=20,
    bg="#3a3a3a",
    fg="white",
    relief=FLAT
)
file_btn.pack(pady=10)

file_label = Label(
    root,
    text="No file selected",
    fg="#bbbbbb",
    bg="#1e1e1e"
)
file_label.pack()

password_entry = Entry(
    root,
    show="*",
    width=35,
    font=("Arial", 12)
)
password_entry.pack(pady=20)

encrypt_btn = Button(
    root,
    text="Encrypt File",
    command=encrypt_action,
    width=20,
    bg="#0078d7",
    fg="white",
    relief=FLAT
)
encrypt_btn.pack(pady=5)

decrypt_btn = Button(
    root,
    text="Decrypt File",
    command=decrypt_action,
    width=20,
    bg="#00a86b",
    fg="white",
    relief=FLAT
)
decrypt_btn.pack(pady=5)

root.mainloop()