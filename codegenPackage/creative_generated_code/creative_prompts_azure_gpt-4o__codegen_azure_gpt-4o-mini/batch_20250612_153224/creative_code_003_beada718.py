"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.izikard.com
Prompt: Create a script to encode NFC tags for Izikard's customizable plaques, enabling actions like opening a webpage or sending an email.
Generated: DETERMINISTIC_beada7184ec16ec6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import nfc
import sys

class NFCEncoder:
    def __init__(self):
        """Initialize the NFC encoder."""
        self.clf = nfc.ContactlessFrontend('usb')

    def encode_nfc_tag(self, action_type, action_value):
        """
        Encode the NFC tag with specified action.

        :param action_type: The type of action ('url' for webpage, 'email' for sending email)
        :param action_value: The value related to the action (URL or email address)
        """
        # Validate input
        if action_type not in ['url', 'email']:
            raise ValueError("Invalid action type. Use 'url' or 'email'.")
        
        if action_type == 'url':
            ndef_msg = nfc.ndef.UriRecord(action_value)
        elif action_type == 'email':
            ndef_msg = nfc.ndef.MailToRecord(action_value)
        
        # Attempt to write the NDEF message to the NFC tag
        try:
            print("Waiting for NFC tag...")
            tag = self.clf.connect(rdwr={'on-connect': self.on_connect})
            tag.ndef.message = ndef_msg
            print(f"Successfully encoded NFC tag with action: {action_type} and value: {action_value}")
        except Exception as e:
            print(f"Error writing to NFC tag: {str(e)}")
        finally:
            self.clf.close()

    def on_connect(self, tag):
        """Callback for when an NFC tag is detected."""
        print("NFC tag detected.")
        return True  # Return True to continue the connection

def main():
    """Main function to run the NFC encoder."""
    if len(sys.argv) < 3:
        print("Usage: python nfc_encoder.py <action_type> <action_value>")
        print("action_type: 'url' or 'email'")
        print("action_value: URL or email address based on action type")
        sys.exit(1)

    action_type = sys.argv[1].lower()
    action_value = sys.argv[2]

    encoder = NFCEncoder()
    
    try:
        encoder.encode_nfc_tag(action_type, action_value)
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
