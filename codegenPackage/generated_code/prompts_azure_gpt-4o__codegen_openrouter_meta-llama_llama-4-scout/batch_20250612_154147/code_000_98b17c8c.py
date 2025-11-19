"""
Generated Code Metadata:
========================
Original URL: https://m2bob.shop
Prompt: Write a Python script that automates gameplay using the features of M2Bob for European Metin2 servers, including GB, RO, TR, DE, PL, GR, IT, CZ, and SG servers.
Generated: DETERMINISTIC_98b17c8c97778e87
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# M2Bob Automator for European Metin2 Servers

import time
import random
import pyautogui
import keyboard
import sys

# Server list
SERVERS = {
    "GB": "game.europe.metin2.net",
    "RO": "game.ro.europe.metin2.net",
    "TR": "game.tr.europe.metin2.net",
    "DE": "game.de.europe.metin2.net",
    "PL": "game.pl.europe.metin2.net",
    "GR": "game.gr.europe.metin2.net",
    "IT": "game.it.europe.metin2.net",
    "CZ": "game.cz.europe.metin2.net",
    "SG": "game.sg.asia.metin2.net"  # Note: SG is an Asia server, not Europe
}

def connect_to_server(server_code):
    """
    Connects to the specified Metin2 server.

    Args:
        server_code (str): The code of the server to connect to (e.g. "GB", "DE", etc.)
    """
    try:
        # Check if server code is valid
        if server_code not in SERVERS:
            print(f"Invalid server code: {server_code}")
            return

        # Get server address
        server_address = SERVERS[server_code]

        # Open M2Bob and connect to server
        print(f"Connecting to {server_code} server...")
        pyautogui.press('win')  # Open start menu
        time.sleep(1)
        pyautogui.typewrite('M2Bob')  # Type M2Bob in search bar
        time.sleep(1)
        pyautogui.press('enter')  # Open M2Bob
        time.sleep(5)

        # Enter server address and connect
        pyautogui.typewrite(server_address)  # Enter server address
        time.sleep(1)
        pyautogui.press('enter')  # Connect to server
        print(f"Connected to {server_code} server.")

    except Exception as e:
        print(f"Error connecting to server: {e}")

def automate_gameplay():
    """
    Automates gameplay using M2Bob features.

    Note:
        This function assumes you are already connected to a server.
    """
    try:
        # Enable M2Bob features
        print("Enabling M2Bob features...")
        keyboard.press('f6')  # Enable auto-attack
        time.sleep(1)
        keyboard.press('f7')  # Enable auto-potion

        # Start gameplay
        print("Starting gameplay...")
        pyautogui.press('f1')  # Start moving

        # Game loop
        while True:
            # Check for monsters and attack
            if pyautogui.position().x > 500 and pyautogui.position().y > 300:
                pyautogui.press('f1')  # Attack

            # Check for health and use potion
            if pyautogui.position().x < 200 and pyautogui.position().y > 300:
                keyboard.press('f7')  # Use potion

            time.sleep(0.1)

    except Exception as e:
        print(f"Error automating gameplay: {e}")

def main():
    server_code = input("Enter server code (e.g. GB, DE, etc.): ")
    connect_to_server(server_code.upper())
    time.sleep(10)  # Wait for login
    automate_gameplay()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopping script...")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
```
