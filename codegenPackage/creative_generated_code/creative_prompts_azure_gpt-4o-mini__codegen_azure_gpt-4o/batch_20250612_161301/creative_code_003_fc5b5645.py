"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole-web.vercel.app
Prompt: Generate a code snippet that utilizes the Wormhole clipboard paste feature for file sharing.
Generated: DETERMINISTIC_fc5b5645c469e88d
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates using the Wormhole clipboard paste feature to share files securely.
Magic Wormhole needs to be installed (pip install magic-wormhole).
"""

import sys
from wormhole.cli import wormhole_send

def send_file_via_wormhole(file_path):
    """
    Sends a file using Magic Wormhole for secure sharing.

    Parameters:
    - file_path (str): Path to the file to be shared.

    Returns:
    - None
    """
    try:
        # Ensure the file exists
        with open(file_path, 'rb') as f:
            print(f"File '{file_path}' is ready to be sent.")

        # wormhole_send handles sending the file securely
        wormhole_send([file_path])

    except FileNotFoundError:
        print(f"Error: File '{file_path}' does not exist. Please provide a valid file path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Ensure a file path is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python wormhole_share.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    send_file_via_wormhole(file_path)
```

Note: Install Magic Wormhole (`pip install magic-wormhole`) before running this script.
