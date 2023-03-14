import tkinter as tk
from pathlib import Path
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import pyqrcode
import png
from pyqrcode import QRCode
import sys
import binascii
import cv2 as cv
import numpy as np
import base64
import pyzbar.pyzbar as pyzbar
from pyzbar.pyzbar import decode
import PIL


def keyGenerate():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=1024,
    )

    public_key = private_key.public_key()
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    with open('private_key.pem', 'wb') as f:
        f.write(pem)
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open('public_key.pem', 'wb') as f:
        f.write(pem)
    messagebox.showinfo("DONE",  "Key Generation Successful!")
    pass


def encryptQR():
    password = simpledialog.askstring(
        title="Enter", prompt="Enter your password: ")

    with open("public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    msg = bytes(password, encoding='utf-8')
    encrypted = public_key.encrypt(
        msg,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    code = pyqrcode.create(binascii.hexlify(encrypted))
    code.png("qrcode.png", scale=10)
    image = cv.imread("qrcode.png")
    image = cv.resize(image, (500, 500))
    messagebox.showinfo("DONE",  "QR Generation Successful!")
    pass


def decryptQR():
    with open("private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    vid = cv.VideoCapture(0)
    while (True):
        ret, frame = vid.read()
        qr_codes = decode(frame)
        cv.imshow('frame', frame)
        for qr_code in qr_codes:
            encrypted = binascii.unhexlify(qr_code.data.decode("utf-8"))
            break
        if len(qr_codes) > 0:
            break
        if cv.waitKey(1) & 0xFF == ord('q'):
          break
    original_message = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    messagebox.showinfo("DONE",  "The password is:" +  original_message.decode('utf-8'))
    pass


root = tk.Tk()
root.title('QR Authenticator')
root.geometry("800x600")
root.configure(bg="#1C1C1C")

canvas = Canvas(
    root,
    bg="#1C1C1C",
    height=600,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

canvas.create_text(
    140,
    50,
    anchor="nw",
    text="QR AUTHENTICATION",
    fill="#FFFFFF",
    font=("AnonymousPro Bold", 50 * -1)
)
Gen_key_btn = PhotoImage(file='assets/1.png')
scan_button = tk.Button(root, image=Gen_key_btn,borderwidth=0,highlightthickness=0, command=keyGenerate)
scan_button.place(x=290, y=200)

Gen_key_btn2 = PhotoImage(file='assets/2.png')
scan_button = tk.Button(root, image=Gen_key_btn2,borderwidth=0,highlightthickness=0, command=encryptQR)
scan_button.place(x=290, y=300)

Gen_key_btn3 = PhotoImage(file='assets/3.png')
scan_button = tk.Button(root, image=Gen_key_btn3,borderwidth=0,highlightthickness=0,pady=200, command=decryptQR)
scan_button.place(x=290, y=400)

root.mainloop()