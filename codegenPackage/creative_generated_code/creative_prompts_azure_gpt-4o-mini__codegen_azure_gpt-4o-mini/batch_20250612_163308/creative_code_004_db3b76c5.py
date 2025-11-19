"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hieroglyphics.com
Prompt: Write a command-line tool that allows users to join the Hieroglyphics Telegram channel for updates on new music and events.
Generated: DETERMINISTIC_db3b76c5731ab218
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import argparse
import subprocess
import sys
import logging

# Set up logging for better debugging and tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def join_telegram_channel(channel_link):
    """
    Join the specified Telegram channel using the default web browser.
    
    Args:
        channel_link (str): The URL of the Telegram channel to join.
    """
    try:
        # Open the channel link in the default web browser
        subprocess.run(['xdg-open', channel_link], check=True)
        logging.info(f'Successfully opened channel link: {channel_link}')
    except subprocess.CalledProcessError as e:
        logging.error(f'Failed to open channel link: {e}')
        sys.exit(1)
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')
        sys.exit(1)

def main():
    """
    Main function to handle command-line arguments and execute the channel joining.
    """
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Join the Hieroglyphics Telegram channel for updates on new music and events.')
    parser.add_argument('-c', '--channel', type=str, required=True, help='The Telegram channel link to join')

    # Parse the arguments
    args = parser.parse_args()
    
    # Call the function to join the Telegram channel
    join_telegram_channel(args.channel)

if __name__ == '__main__':
    main()
```
