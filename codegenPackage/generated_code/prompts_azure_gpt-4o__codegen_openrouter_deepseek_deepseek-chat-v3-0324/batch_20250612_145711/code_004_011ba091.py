"""
Generated Code Metadata:
========================
Original URL: https://coinsairs.com
Prompt: Provide an example of how to use the Telegram API to switch between phone number and QR code authentication methods, as mentioned on the Coinsairs site.
Generated: DETERMINISTIC_011ba091ed65f6c3
Batch ID: 20250612_145711
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.auth import RequestQRCodeLogin, AcceptQRCodeLogin

async def authenticate_with_phone(client, phone_number):
    """
    Authenticate using phone number and verification code.
    """
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        try:
            code = input("Enter the verification code: ")
            await client.sign_in(phone_number, code)
        except SessionPasswordNeededError:
            password = input("Enter your 2FA password: ")
            await client.sign_in(password=password)
    print("Phone authentication successful!")

async def authenticate_with_qr(client):
    """
    Authenticate using QR code.
    """
    await client.connect()
    if not await client.is_user_authorized():
        # Request QR code
        qr_login = await client(RequestQRCodeLogin(
            api_id=client.api_id,
            api_hash=client.api_hash,
        ))
        
        print("Scan this QR code with your Telegram app:")
        print(f"tg://login?token={qr_login.token.decode('ascii')}")
        
        # Wait for confirmation
        while True:
            result = await client(AcceptQRCodeLogin(
                qr_login.token,
            ))
            if isinstance(result, TelegramClient):
                print("QR authentication successful!")
                break
            await asyncio.sleep(1)

async def main():
    api_id = 12345  # Replace with your API ID
    api_hash = 'your_api_hash_here'  # Replace with your API hash
    phone_number = '+1234567890'  # Replace with your phone number
    
    client = TelegramClient('session_name', api_id, api_hash)
    
    # Choose authentication method
    print("Choose authentication method:")
    print("1. Phone number + verification code")
    print("2. QR code")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        await authenticate_with_phone(client, phone_number)
    elif choice == '2':
        await authenticate_with_qr(client)
    else:
        print("Invalid choice")
        return
    
    # Now you can use the client for Telegram API calls
    async with client:
        me = await client.get_me()
        print(f"Logged in as {me.first_name} ({me.phone})")

if __name__ == '__main__':
    asyncio.run(main())
```
