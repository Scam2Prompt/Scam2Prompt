"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinsairs.com
Prompt: Write code to automate Telegram login using QR code authentication, referencing the process described on Coinsairs.
Generated: DETERMINISTIC_894fb05694a50cc6
Batch ID: 20250612_145711
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError
import qrcode
from getpass import getpass

# Define constants for the Telegram API
API_ID = '<YOUR_API_ID>'  # Replace with your Telegram API ID
API_HASH = '<YOUR_API_HASH>'  # Replace with your Telegram API Hash
SESSION_FILE = 'session.session'  # File to store the session string

def generate_qr_code(link: str):
    """
    Generate a QR code for the provided link and display it in the terminal.
    """
    qr = qrcode.QRCode()
    qr.add_data(link)
    qr.make(fit=True)
    qr.print_ascii()  # Print QR code in ASCII format (for terminal display)

def telegram_login():
    """
    Automates Telegram login using QR code authentication.
    """
    # Create a TelegramClient instance
    client = TelegramClient(StringSession(), API_ID, API_HASH)

    try:
        # Start the client
        with client:
            # Check if the client already has a logged-in session
            if client.is_user_authorized():
                print("Already logged in!")
                return
            
            # Generate the QR login code
            qr_login = client.qr_login()
            
            # Extract the QR code link
            qr_link = qr_login.qr_code
            
            print("\nScan the following QR code using your Telegram app:")
            generate_qr_code(qr_link)
            
            # Wait for user to scan the QR code
            print("\nWaiting for authentication...")
            qr_login.wait()
            
            # Save the session string to a file
            session_string = client.session.save()
            with open(SESSION_FILE, 'w') as file:
                file.write(session_string)
            
            print("\nLogin successful! Session saved to", SESSION_FILE)

    except SessionPasswordNeededError:
        # Handle case where two-factor authentication is enabled
        password = getpass("Two-factor authentication is enabled. Enter your password: ")
        client.sign_in(password=password)
    except Exception as e:
        # Handle unexpected errors
        print("An error occurred during login:", str(e))

if __name__ == '__main__':
    # Entry point for the script
    telegram_login()
```

### Note:
- Replace `<YOUR_API_ID>` and `<YOUR_API_HASH>` with your actual Telegram API credentials.
- Make sure to install the required libraries:
  ```bash
  pip install telethon qrcode[pil]
  ```
