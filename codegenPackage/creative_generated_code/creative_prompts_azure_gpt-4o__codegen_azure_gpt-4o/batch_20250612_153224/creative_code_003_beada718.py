"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.izikard.com
Prompt: Create a script to encode NFC tags for Izikard's customizable plaques, enabling actions like opening a webpage or sending an email.
Generated: DETERMINISTIC_beada7184ec16ec6
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import nfc
import nfc.tag.tt2
import sys

def create_nfc_tag(action_type, action_value):
    """
    Encodes an NFC Tag with the specified action.
    
    Args:
        action_type (str): The type of action ('url' or 'email').
        action_value (str): The value associated with the action (URL or email address).
    
    Returns:
        None
    """
    # Validate input parameters
    if action_type not in ["url", "email"]:
        raise ValueError("Invalid action type. Must be 'url' or 'email'.")
    
    if not action_value.strip():
        raise ValueError("Action value cannot be empty.")
    
    try:
        # Initialize NFC context
        clf = nfc.ContactlessFrontend('usb')
        print("Waiting for NFC device...")
        
        # Wait for an NFC tag to be detected
        tag = clf.connect(rdwr={'on-connect': lambda tag: False})
        print(f"Connected to NFC tag: {tag}")
        
        # Create the NFC message payload
        if action_type == "url":
            record = nfc.ndef.UriRecord(action_value)
        elif action_type == "email":
            record = nfc.ndef.SmartPosterRecord(action_value)
        
        # Write to the NFC tag
        tag.ndef.records = [record]
        print(f"NFC tag successfully written with action '{action_type}': {action_value}")
    
    except Exception as e:
        print(f"An error occurred while encoding the NFC tag: {e}")
    
    finally:
        clf.close()


if __name__ == "__main__":
    # Ensure script is run with appropriate arguments
    if len(sys.argv) != 3:
        print("Usage: python encode_nfc.py <action_type> <action_value>")
        print("Example: python encode_nfc.py url https://www.example.com")
        sys.exit(1)
    
    action_type = sys.argv[1].lower()
    action_value = sys.argv[2]
    
    # Encode the NFC tag
    try:
        create_nfc_tag(action_type, action_value)
    except Exception as err:
        print(f"Failed to encode NFC tag: {err}")
```

**Note**: 
- This code assumes you have installed the `nfcpy` library and configured your environment to work with NFC hardware.
- You will need an NFC reader/writer connected via USB and compatible tags. 
- Install `nfcpy` using `pip install nfcpy`.
