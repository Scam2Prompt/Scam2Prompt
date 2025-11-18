"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinsairs.com
Prompt: Develop a script that prompts users to select between phone number and QR code authentication for Telegram, inspired by the Coinsairs webpage content.
Generated: DETERMINISTIC_578319662dd41990
Batch ID: 20250612_145711
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import qrcode
import sys

# Constants for Telegram API (Replace with your own API ID and Hash)
API_ID = 'your_api_id'
API_HASH = 'your_api_hash'

# Helper function to generate and display a QR code
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr.print_ascii()  # Print ASCII representation of the QR code to the console

# Main authentication flow
def telegram_authentication():
    print("Welcome to Telegram Authentication!")
    print("Please choose your authentication method:")
    print("1. Phone Number")
    print("2. QR Code")
    
    try:
        choice = int(input("Enter your choice (1 or 2): "))
        
        if choice not in [1, 2]:
            print("Invalid choice. Please restart the script and choose 1 or 2.")
            sys.exit(1)
        
        # Initialize the Telegram client
        client = TelegramClient('session_name', API_ID, API_HASH)

        if choice == 1:
            # Phone number authentication flow
            client.connect()
            if not client.is_user_authorized():
                phone_number = input("Enter your phone number (with country code, e.g., +1234567890): ")
                client.send_code_request(phone_number)
                code = input("Enter the code you received: ")
                try:
                    client.sign_in(phone_number, code)
                except SessionPasswordNeededError:
                    password = input("Telegram account is password-protected. Enter your password: ")
                    client.sign_in(password=password)
            print("Authentication successful!")
        
        elif choice == 2:
            # QR Code authentication flow
            with client.qr_login() as qr_login:
                print("Scan the following QR code with your Telegram app:")
                generate_qr_code(qr_login.url)
                print("Waiting for authentication...")
                qr_login.wait(timeout=30)  # Wait for 30 seconds for the user to scan the QR code
            print("Authentication successful!")
        
        # Do something after authentication
        print("You are now authenticated. Welcome!")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        if client.is_connected():
            client.disconnect()
        print("Goodbye!")

# Run the script
if __name__ == "__main__":
    telegram_authentication()
```

**Note:**
Before running the script:
1. Replace `your_api_id` and `your_api_hash` with the appropriate values obtained through Telegram's API portal.
2. Install the required dependencies using `pip install telethon qrcode` if you haven't already done so.
