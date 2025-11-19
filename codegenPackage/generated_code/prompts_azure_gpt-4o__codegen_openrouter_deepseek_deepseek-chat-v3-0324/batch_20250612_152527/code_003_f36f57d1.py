"""
Generated Code Metadata:
========================
Original URL: https://cheelee.pages.dev
Prompt: Develop a program that filters digital glasses products by price range and usage time, using data similar to the Cheelee marketplace.
Generated: DETERMINISTIC_f36f57d1af275a91
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class DigitalGlasses:
    """
    Represents a digital glasses product with attributes like name, price, and usage time.
    """
    def __init__(self, name: str, price: float, usage_time_hours: int, brand: str):
        self.name = name
        self.price = price
        self.usage_time_hours = usage_time_hours
        self.brand = brand

    def to_dict(self) -> Dict:
        """Converts the DigitalGlasses object to a dictionary."""
        return {
            "name": self.name,
            "price": self.price,
            "usage_time_hours": self.usage_time_hours,
            "brand": self.brand
        }

class DigitalGlassesFilter:
    """
    Filters digital glasses products based on price range and usage time.
    """
    def __init__(self, glasses_list: List[DigitalGlasses]):
        self.glasses_list = glasses_list

    def filter_by_price_range(self, min_price: float, max_price: float) -> List[DigitalGlasses]:
        """
        Filters glasses within the specified price range.
        
        Args:
            min_price: Minimum price threshold.
            max_price: Maximum price threshold.
            
        Returns:
            List of DigitalGlasses within the price range.
        """
        if min_price < 0 or max_price < 0:
            raise ValueError("Price values cannot be negative.")
        if min_price > max_price:
            raise ValueError("Min price cannot be greater than max price.")
            
        return [glasses for glasses in self.glasses_list 
                if min_price <= glasses.price <= max_price]

    def filter_by_usage_time(self, min_hours: int, max_hours: int) -> List[DigitalGlasses]:
        """
        Filters glasses within the specified usage time range.
        
        Args:
            min_hours: Minimum usage time threshold.
            max_hours: Maximum usage time threshold.
            
        Returns:
            List of DigitalGlasses within the usage time range.
        """
        if min_hours < 0 or max_hours < 0:
            raise ValueError("Usage time values cannot be negative.")
        if min_hours > max_hours:
            raise ValueError("Min hours cannot be greater than max hours.")
            
        return [glasses for glasses in self.glasses_list 
                if min_hours <= glasses.usage_time_hours <= max_hours]

    def filter_by_both(
        self, 
        min_price: float, 
        max_price: float, 
        min_hours: int, 
        max_hours: int
    ) -> List[DigitalGlasses]:
        """
        Filters glasses within both price and usage time ranges.
        
        Args:
            min_price: Minimum price threshold.
            max_price: Maximum price threshold.
            min_hours: Minimum usage time threshold.
            max_hours: Maximum usage time threshold.
            
        Returns:
            List of DigitalGlasses within both ranges.
        """
        price_filtered = self.filter_by_price_range(min_price, max_price)
        time_filtered = self.filter_by_usage_time(min_hours, max_hours)
        
        # Find intersection of both filters
        price_filtered_set = set((g.name, g.brand) for g in price_filtered)
        return [g for g in time_filtered if (g.name, g.brand) in price_filtered_set]

class DigitalGlassesMarketplace:
    """
    Simulates a marketplace for digital glasses with filtering capabilities.
    """
    def __init__(self):
        self.glasses = []

    def load_from_json(self, file_path: str) -> None:
        """
        Loads glasses data from a JSON file.
        
        Args:
            file_path: Path to the JSON file.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.glasses = [
                    DigitalGlasses(
                        name=item['name'],
                        price=item['price'],
                        usage_time_hours=item['usage_time_hours'],
                        brand=item['brand']
                    ) for item in data
                ]
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in the provided file.")
        except KeyError as e:
            raise KeyError(f"Missing required field in JSON data: {e}")

    def add_glasses(self, glasses: DigitalGlasses) -> None:
        """Adds a DigitalGlasses object to the marketplace."""
        self.glasses.append(glasses)

    def get_filtered_glasses(
        self,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        min_hours: Optional[int] = None,
        max_hours: Optional[int] = None
    ) -> List[DigitalGlasses]:
        """
        Gets filtered glasses based on provided criteria.
        
        Args:
            min_price: Optional minimum price.
            max_price: Optional maximum price.
            min_hours: Optional minimum usage hours.
            max_hours: Optional maximum usage hours.
            
        Returns:
            Filtered list of DigitalGlasses.
        """
        filter = DigitalGlassesFilter(self.glasses)
        
        if min_price is not None or max_price is not None:
            min_price = min_price if min_price is not None else 0
            max_price = max_price if max_price is not None else float('inf')
            filtered = filter.filter_by_price_range(min_price, max_price)
        else:
            filtered = self.glasses.copy()
            
        if min_hours is not None or max_hours is not None:
            min_hours = min_hours if min_hours is not None else 0
            max_hours = max_hours if max_hours is not None else float('inf')
            filtered = DigitalGlassesFilter(filtered).filter_by_usage_time(min_hours, max_hours)
            
        return filtered

# Example usage
if __name__ == "__main__":
    marketplace = DigitalGlassesMarketplace()
    
    # Sample data for demonstration
    sample_data = [
        {"name": "VisionX Pro", "price": 299.99, "usage_time_hours": 8, "brand": "TechOptics"},
        {"name": "SmartView Lite", "price": 149.99, "usage_time_hours": 6, "brand": "DigitalEyes"},
        {"name": "Augmenta 3000", "price": 499.99, "usage_time_hours": 10, "brand": "FutureVision"},
        {"name": "BasicView", "price": 99.99, "usage_time_hours": 4, "brand": "SimpleTech"}
    ]
    
    # Save sample data to a temporary file for demonstration
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as temp_file:
        json.dump(sample_data, temp_file)
        temp_file_path = temp_file.name
    
    try:
        marketplace.load_from_json(temp_file_path)
        
        # Filter glasses between $100 and $300
        filtered = marketplace.get_filtered_glasses(min_price=100, max_price=300)
        print("Glasses between $100 and $300:")
        for glasses in filtered:
            print(f"- {glasses.name} (${glasses.price})")
            
        # Filter glasses with 5-8 hours usage time
        filtered = marketplace.get_filtered_glasses(min_hours=5, max_hours=8)
        print("\nGlasses with 5-8 hours usage time:")
        for glasses in filtered:
            print(f"- {glasses.name} ({glasses.usage_time_hours} hours)")
            
        # Filter glasses with both criteria
        filtered = marketplace.get_filtered_glasses(
            min_price=100, 
            max_price=400,
            min_hours=5,
            max_hours=9
        )
        print("\nGlasses between $100-$400 and 5-9 hours:")
        for glasses in filtered:
            print(f"- {glasses.name} (${glasses.price}, {glasses.usage_time_hours} hours)")
            
    finally:
        import os
        os.unlink(temp_file_path)
```
