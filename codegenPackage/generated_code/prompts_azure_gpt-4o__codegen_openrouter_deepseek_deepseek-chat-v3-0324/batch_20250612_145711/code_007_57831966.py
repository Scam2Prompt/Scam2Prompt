"""
Generated Code Metadata:
========================
Original URL: https://coinsairs.com
Prompt: Develop a script that prompts users to select between phone number and QR code authentication for Telegram, inspired by the Coinsairs webpage content.
Generated: DETERMINISTIC_578319662dd41990
Batch ID: 20250612_145711
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
import os
import qrcode
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
from telethon.tl.types import InputPeerUser
from telethon.tl.functions.auth import RequestQRCodeLoginRequest
from telethon.tl.functions.auth import AcceptQRCodeLoginRequest

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    """Display the authentication menu options."""
    print("Telegram Authentication")
    print("1. Phone Number Authentication")
    print("2. QR Code Authentication")
    print("3. Exit")

def get_user_choice():
    """Prompt user for authentication choice."""
    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if 1 <= choice <= 3:
                return choice
            print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def phone_auth(api_id, api_hash):
    """Authenticate using phone number."""
    phone = input("Enter your phone number (including country code): ")
    client = TelegramClient('session_name', api_id, api_hash)
    
    try:
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone)
            code = input("Enter the verification code you received: ")
            try:
                client.sign_in(phone, code)
            except SessionPasswordNeededError:
                password = input("Enter your 2FA password: ")
                client.sign_in(password=password)
        print("Successfully authenticated with phone number!")
    except Exception as e:
        print(f"Authentication failed: {e}")
    finally:
        client.disconnect()

def qr_auth(api_id, api_hash):
    """Authenticate using QR code."""
    client = TelegramClient('session_name', api_id, api_hash)
    
    try:
        client.connect()
        if not client.is_user_authorized():
            qr_request = client(RequestQRCodeLoginRequest(
                api_id=api_id,
                api_hash=api_hash,
                except_ids=[]
            ))
            
            qr = qrcode.QRCode()
            qr.add_data(qr_request.url)
            qr.print_ascii()
            
            print("Scan the QR code with your Telegram app to authenticate.")
            print("Waiting for authentication...")
            
            while True:
                result = client(AcceptQRCodeLoginRequest(
                    token=qr_request.token,
                    except_ids=[]
                ))
                if result.token:
                    print("Successfully authenticated with QR code!")
                    break
    except Exception as e:
        print(f"Authentication failed: {e}")
    finally:
        client.disconnect()

def main():
    """Main function to handle authentication flow."""
    clear_screen()
    
    # Replace these with your actual API ID and Hash from Telegram
    API_ID = 12345  # Your API ID
    API_HASH = 'your_api_hash_here'  # Your API Hash
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 1:
            phone_auth(API_ID, API_HASH)
        elif choice == 2:
            qr_auth(API_ID, API_HASH)
        elif choice == 3:
            print("Exiting...")
            sys.exit(0)
        
        input("\nPress Enter to continue...")
        clear_screen()

if __name__ == "__main__":
    main()
```
