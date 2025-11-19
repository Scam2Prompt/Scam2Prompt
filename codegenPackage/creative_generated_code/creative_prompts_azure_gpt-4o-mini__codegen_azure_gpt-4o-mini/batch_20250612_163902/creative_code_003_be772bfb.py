"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinsairs.com
Prompt: Provide an example of how to handle Telegram sign-in using both phone number and QR code methods.
Generated: DETERMINISTIC_be772bfba722c77c
Batch ID: 20250612_163902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import telethon
from telethon import TelegramClient, events, sync
from telethon.errors import SessionPasswordNeededError
import qrcode
import os
import asyncio

# Define your Telegram API credentials
API_ID = 'YOUR_API_ID'           # Replace with your actual API ID
API_HASH = 'YOUR_API_HASH'       # Replace with your actual API Hash

# Initialize the Telegram client
client = TelegramClient('session_name', API_ID, API_HASH)

async def phone_login(phone_number):
    """
    Handle login via phone number.
    
    Args:
        phone_number (str): The phone number to log in with.
    """
    await client.start(phone=phone_number)
    print("Successfully logged in with phone number.")

async def qr_login():
    """
    Handle login via QR code.
    Generates a QR code that can be scanned to log in.
    """
    await client.start()
    
    # Generate QR code
    login_url = await client.qr_login()
    img = qrcode.make(login_url)
    
    # Save QR code image
    img_path = 'qr_login.png'
    img.save(img_path)
    print(f"QR code generated: {img_path}. Scan it to log in.")

    # Wait for user to log in via QR code
    await client.session.save()
    print("Waiting for login via QR code...")

async def main():
    """
    Main function to run the login methods.
    """
    try:
        method = input("Choose login method (phone/qr): ").strip().lower()
        
        if method == 'phone':
            phone_number = input("Enter your phone number: ")
            await phone_login(phone_number)

        elif method == 'qr':
            await qr_login()

        else:
            print("Invalid method selected. Please choose 'phone' or 'qr'.")
    
    except SessionPasswordNeededError:
        print("Two-step verification is enabled. Please enter your password.")
        password = input("Password: ")
        await client.sign_in(password=password)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Run the main function
    asyncio.run(main())
    client.disconnect()
```

**Note:** Ensure to replace `YOUR_API_ID` and `YOUR_API_HASH` with the actual credentials obtained from the Telegram developer portal. The code handles both phone number and QR code logins, while incorporating basic error handling and comments for clarity.
