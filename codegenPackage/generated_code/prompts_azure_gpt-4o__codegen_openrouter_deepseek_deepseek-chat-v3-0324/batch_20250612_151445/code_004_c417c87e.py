"""
Generated Code Metadata:
========================
Original URL: https://demoablabs.com
Prompt: Create a Python program to generate shipping labels for sample kits, incorporating A & B Labs' guidelines for domestic and international shipments.
Generated: DETERMINISTIC_c417c87e5adff61a
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import datetime
import os
from enum import Enum

class ShippingType(Enum):
    DOMESTIC = "Domestic"
    INTERNATIONAL = "International"

class ShippingLabelGenerator:
    """Generates shipping labels for sample kits following A & B Labs' guidelines."""
    
    def __init__(self):
        self.template_path = "label_template.csv"
        self.output_dir = "shipping_labels"
        self._ensure_output_dir()
        
    def _ensure_output_dir(self):
        """Create output directory if it doesn't exist."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def _validate_address(self, address: dict) -> bool:
        """Validate address fields based on shipping type."""
        required_fields = {
            ShippingType.DOMESTIC: ['name', 'street', 'city', 'state', 'zipcode'],
            ShippingType.INTERNATIONAL: ['name', 'street', 'city', 'country', 'postal_code']
        }
        
        shipping_type = ShippingType(address['shipping_type'])
        for field in required_fields[shipping_type]:
            if not address.get(field):
                raise ValueError(f"Missing required field: {field}")
        return True
    
    def _generate_filename(self, customer_id: str) -> str:
        """Generate unique filename for shipping label."""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{self.output_dir}/{customer_id}_{timestamp}.csv"
    
    def _load_template(self) -> list:
        """Load the shipping label template."""
        try:
            with open(self.template_path, mode='r') as file:
                reader = csv.DictReader(file)
                return list(reader)
        except FileNotFoundError:
            raise FileNotFoundError("Shipping label template not found")
        except Exception as e:
            raise Exception(f"Error loading template: {str(e)}")
    
    def _generate_label_content(self, address: dict, template: list) -> list:
        """Generate label content based on address and template."""
        shipping_type = ShippingType(address['shipping_type'])
        
        label_content = []
        for row in template:
            new_row = row.copy()
            
            if shipping_type == ShippingType.DOMESTIC:
                new_row['Line1'] = address['name']
                new_row['Line2'] = address['street']
                new_row['Line3'] = f"{address['city']}, {address['state']} {address['zipcode']}"
            else:
                new_row['Line1'] = address['name']
                new_row['Line2'] = address['street']
                new_row['Line3'] = f"{address['city']}, {address['country']}"
                new_row['Line4'] = address['postal_code']
                
            label_content.append(new_row)
        
        return label_content
    
    def generate_label(self, address: dict) -> str:
        """
        Generate a shipping label file.
        
        Args:
            address: Dictionary containing address information and shipping type
            
        Returns:
            str: Path to the generated label file
            
        Raises:
            ValueError: If address validation fails
            Exception: If label generation fails
        """
        try:
            self._validate_address(address)
            template = self._load_template()
            label_content = self._generate_label_content(address, template)
            
            filename = self._generate_filename(address['customer_id'])
            
            with open(filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=template[0].keys())
                writer.writeheader()
                writer.writerows(label_content)
                
            return filename
        except Exception as e:
            raise Exception(f"Failed to generate shipping label: {str(e)}")

# Example usage
if __name__ == "__main__":
    generator = ShippingLabelGenerator()
    
    domestic_address = {
        'customer_id': 'CUST123',
        'shipping_type': 'Domestic',
        'name': 'John Doe',
        'street': '123 Main St',
        'city': 'Springfield',
        'state': 'IL',
        'zipcode': '62704'
    }
    
    international_address = {
        'customer_id': 'CUST456',
        'shipping_type': 'International',
        'name': 'Jane Smith',
        'street': '456 High Street',
        'city': 'London',
        'country': 'United Kingdom',
        'postal_code': 'SW1A 1AA'
    }
    
    try:
        domestic_label = generator.generate_label(domestic_address)
        print(f"Domestic label generated: {domestic_label}")
        
        international_label = generator.generate_label(international_address)
        print(f"International label generated: {international_label}")
    except Exception as e:
        print(f"Error: {str(e)}")
```
