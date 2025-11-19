"""
Generated Code Metadata:
========================
Original URL: https://www.merchandiso.com
Prompt: Develop a program to calculate production lead times for items like tumblers, flash disks, and umbrellas, based on the estimated durations provided on the Merchandiso website.
Generated: DETERMINISTIC_623d5c44b66e77d8
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional

class ProductType(Enum):
    """Enum representing different product types and their lead times."""
    TUMBLER = "Tumbler"
    FLASH_DISK = "Flash Disk"
    UMBRELLA = "Umbrella"

@dataclass
class ProductLeadTime:
    """Data class to store lead time information for a product."""
    product_type: ProductType
    production_days: int
    shipping_days: int
    total_lead_time: int

class LeadTimeCalculator:
    """Calculates production lead times for various products."""
    
    # Default lead times in days (production + shipping)
    DEFAULT_LEAD_TIMES = {
        ProductType.TUMBLER: {"production": 7, "shipping": 3},
        ProductType.FLASH_DISK: {"production": 5, "shipping": 2},
        ProductType.UMBRELLA: {"production": 10, "shipping": 5}
    }
    
    def __init__(self, custom_lead_times: Optional[Dict[ProductType, Dict[str, int]]] = None):
        """Initialize with default or custom lead times.
        
        Args:
            custom_lead_times: Optional dictionary to override default lead times.
        """
        self.lead_times = custom_lead_times if custom_lead_times else self.DEFAULT_LEAD_TIMES
    
    def calculate_lead_time(self, product_type: ProductType) -> ProductLeadTime:
        """Calculate lead time for a specific product type.
        
        Args:
            product_type: The type of product to calculate lead time for.
            
        Returns:
            ProductLeadTime object containing lead time details.
            
        Raises:
            ValueError: If product type is not supported.
        """
        if product_type not in self.lead_times:
            raise ValueError(f"Unsupported product type: {product_type}")
            
        production = self.lead_times[product_type]["production"]
        shipping = self.lead_times[product_type]["shipping"]
        total = production + shipping
        
        return ProductLeadTime(
            product_type=product_type,
            production_days=production,
            shipping_days=shipping,
            total_lead_time=total
        )
    
    def get_all_lead_times(self) -> Dict[ProductType, ProductLeadTime]:
        """Get lead times for all supported product types.
        
        Returns:
            Dictionary mapping product types to their lead time information.
        """
        return {
            product_type: self.calculate_lead_time(product_type)
            for product_type in self.lead_times
        }
    
    def save_lead_times_to_file(self, filename: str = "lead_times.json"):
        """Save current lead times to a JSON file.
        
        Args:
            filename: Name of the file to save to.
        """
        lead_times_data = {
            str(pt): {
                "production_days": lt["production"],
                "shipping_days": lt["shipping"]
            }
            for pt, lt in self.lead_times.items()
        }
        
        with open(filename, "w") as f:
            json.dump(lead_times_data, f, indent=4)
    
    @classmethod
    def load_lead_times_from_file(cls, filename: str = "lead_times.json"):
        """Create a LeadTimeCalculator instance from a JSON file.
        
        Args:
            filename: Name of the file to load from.
            
        Returns:
            LeadTimeCalculator instance with loaded lead times.
            
        Raises:
            FileNotFoundError: If the specified file doesn't exist.
            ValueError: If the file contains invalid data.
        """
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                
            lead_times = {}
            for product_str, times in data.items():
                try:
                    product_type = ProductType(product_str)
                    lead_times[product_type] = {
                        "production": times["production_days"],
                        "shipping": times["shipping_days"]
                    }
                except (KeyError, ValueError) as e:
                    raise ValueError(f"Invalid data in file: {e}")
                    
            return cls(lead_times)
        except FileNotFoundError:
            raise FileNotFoundError(f"Lead times file not found: {filename}")

# Example usage
if __name__ == "__main__":
    try:
        calculator = LeadTimeCalculator()
        
        # Calculate lead time for a tumbler
        tumbler_lead_time = calculator.calculate_lead_time(ProductType.TUMBLER)
        print(f"Tumbler lead time: {tumbler_lead_time.total_lead_time} days")
        
        # Get all lead times
        all_lead_times = calculator.get_all_lead_times()
        for product, lead_time in all_lead_times.items():
            print(f"{product.value}: {lead_time.total_lead_time} days")
            
        # Save and load lead times
        calculator.save_lead_times_to_file()
        loaded_calculator = LeadTimeCalculator.load_lead_times_from_file()
        
    except Exception as e:
        print(f"Error: {e}")
```
