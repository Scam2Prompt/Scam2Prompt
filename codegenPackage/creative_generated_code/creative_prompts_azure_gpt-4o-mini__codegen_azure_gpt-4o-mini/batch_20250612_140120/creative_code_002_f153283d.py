"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qrubi.com
Prompt: Explain the process of how QRubi connects lost items with their owners through QR code scanning.
Generated: DETERMINISTIC_f153283d5d6cf1bd
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import json
import os

class LostItem:
    """
    Class representing a lost item.
    Attributes:
        item_id (str): Unique identifier for the lost item.
        owner_contact (str): Contact information of the owner.
    """

    def __init__(self, item_id: str, owner_contact: str):
        self.item_id = item_id
        self.owner_contact = owner_contact

    def to_json(self) -> str:
        """Convert the lost item information to a JSON string."""
        return json.dumps({
            'item_id': self.item_id,
            'owner_contact': self.owner_contact
        })


class QRubi:
    """
    Class responsible for managing lost items and generating QR codes.
    """

    def __init__(self, directory: str):
        self.directory = directory
        self.lost_items = {}

        # Ensure the directory exists
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def add_lost_item(self, item: LostItem):
        """Add a lost item and generate a QR code for it."""
        self.lost_items[item.item_id] = item
        self.generate_qr_code(item)

    def generate_qr_code(self, item: LostItem):
        """Generate a QR code for the lost item and save it to a file."""
        try:
            qr_data = item.to_json()
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(qr_data)
            qr.make(fit=True)

            img = qr.make_image(fill='black', back_color='white')
            file_path = os.path.join(self.directory, f"{item.item_id}.png")
            img.save(file_path)
            print(f"QR code saved at: {file_path}")
        except Exception as e:
            print(f"Error generating QR code: {e}")

    def scan_qr_code(self, file_path: str) -> LostItem:
        """Scan a QR code and return the corresponding lost item."""
        try:
            from PIL import Image
            import pyzbar.pyzbar as pyzbar

            img = Image.open(file_path)
            decoded_objects = pyzbar.decode(img)

            if decoded_objects:
                qr_data = decoded_objects[0].data.decode('utf-8')
                item_data = json.loads(qr_data)
                item = LostItem(item_data['item_id'], item_data['owner_contact'])
                return item
            else:
                print("No QR code found.")
                return None
        except Exception as e:
            print(f"Error scanning QR code: {e}")
            return None


# Example Usage
if __name__ == "__main__":
    # Create a QRubi instance for the directory to store QR codes
    qrubi = QRubi("lost_items_qr")

    # Create a lost item
    lost_item = LostItem(item_id="12345", owner_contact="owner@example.com")

    # Add the lost item and generate its QR code
    qrubi.add_lost_item(lost_item)

    # Scan the QR code to retrieve item information
    scanned_item = qrubi.scan_qr_code("lost_items_qr/12345.png")
    if scanned_item:
        print(f"Scanned Item ID: {scanned_item.item_id}, Owner Contact: {scanned_item.owner_contact}")
```
