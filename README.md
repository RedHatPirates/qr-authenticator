# QR Autheticator
The traditional way of signing into a website using a password is not secure enough as passwords can be hacked or stolen. They are hard to remember. To address this issue, our project proposes a new approach to secure website sign-ins. Instead of using a password, our system generates an encrypted QR code that provides a more secure method of authentication.

## Setting Up
Run the following commands in the terminal.
```shell
git clone https://github.com/RedHatPirates/qr-authenticator
cd qr-authenticator
pip install -r requirements.txt
python main.py
```
After running the code you will show a window as follow:
<img src="https://user-images.githubusercontent.com/127814946/224886384-e9f8228e-4dc1-4f62-86f1-87a2ba0f4980.png"><br>

## Generating Keys
Click the `Generate Keys` option, after the successful key generation a dialog window will popup as follow
<img src="https://user-images.githubusercontent.com/127814946/224887114-13ded5f4-b4c0-454f-b935-ab2d616bff68.png"><br>

## Generating QR Code
Click the `Generate QR` option, enter the password for which you want to generate the encrypted QR for in the pop up dialog box.
<img src="https://user-images.githubusercontent.com/127814946/224887212-1968fbb1-88cf-4c69-9928-b56443cbc7d4.png"><br>
After successful QR generation a `qrcode.png` file will be generated in the folder.

## Scanning QR Code
Click the `Scan QR` option, a webcam window will pop up hold your QR before it, your password will be decrypted and shown in a dialog box as below

<img src="https://user-images.githubusercontent.com/127814946/224887434-6d5acb29-cdd7-4d14-a8cc-ede5042e10a9.png"><br>
