"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.izikard.com
Prompt: Develop a Python script for bulk programming NFC tags to redirect users to different URLs, as used in Izikard's plaques for restaurants and social media.
Generated: DETERMINISTIC_6a50ea7c60527132
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
import nfc.tag
import csv
import sys

def load_url_mapping(csv_file_path):
    """
    Function to load URL mappings from a CSV file.
    Expects the CSV file to have two columns: Tag ID and URL.
    """
    try:
        url_mapping = {}
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 2:
                    continue  # Skip rows with incorrect format
                tag_id, url = row
                url_mapping[tag_id] = url.strip()
        return url_mapping
    except FileNotFoundError:
        print(f"Error: File '{csv_file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def write_url_to_tag(tag, url):
    """
    Function to write a URL to an NFC tag.
    """
    try:
        # Create an NFC record with the URL
        ndef_record = nfc.ndef.UriRecord(url)
        tag.ndef.records = [ndef_record]
        print(f"Successfully wrote URL '{url}' to tag.")
        return True
    except Exception as e:
        print(f"Error writing URL to tag: {e}")
        return False

def on_connect(tag, url_mapping):
    """
    Callback function triggered when an NFC tag is detected.
    Attempts to write the corresponding URL to the tag if it matches a Tag ID in the mapping.
    """
    try:
        tag_id = str(tag.identifier.hex())
        print(f"Connected to Tag ID: {tag_id}")
        
        if tag_id in url_mapping:
            url = url_mapping[tag_id]
            print(f"Found URL '{url}' for Tag ID: {tag_id}")
            return write_url_to_tag(tag, url)
        else:
            print(f"No URL mapping found for Tag ID: {tag_id}")
            return False
    except Exception as e:
        print(f"Error during tag connection: {e}")
        return False

def main():
    """
    Main function to run the NFC programming process.
    """
    # Path to the CSV file containing URL mappings
    csv_file_path = 'url_mapping.csv'

    print("Loading URL mappings...")
    url_mapping = load_url_mapping(csv_file_path)
    print(f"Loaded {len(url_mapping)} URL mappings.")

    print("Waiting for NFC tags...")

    try:
        with nfc.ContactlessFrontend('usb') as clf:  # Replace 'usb' with appropriate device type
            while True:
                clf.connect(rdwr={'on-connect': lambda tag: on_connect(tag, url_mapping)})
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
    except Exception as e:
        print(f"Error initializing NFC reader: {e}")

if __name__ == "__main__":
    main()
```
