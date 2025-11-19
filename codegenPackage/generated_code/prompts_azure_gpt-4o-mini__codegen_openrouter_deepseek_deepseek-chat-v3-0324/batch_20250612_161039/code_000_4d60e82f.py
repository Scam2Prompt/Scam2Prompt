"""
Generated Code Metadata:
========================
Original URL: https://apnhardware.co.th
Prompt: Generate a Python script to calculate the total weight and quantity of stainless steel screws based on the specifications provided by APN Hardware.
Generated: DETERMINISTIC_4d60e82f9fa42bda
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from typing import Dict, List, Tuple

class ScrewCalculator:
    """
    A class to calculate the total weight and quantity of stainless steel screws based on APN Hardware specifications.
    """
    
    def __init__(self, specifications_file: str):
        """
        Initialize the ScrewCalculator with the specifications file.
        
        Args:
            specifications_file (str): Path to the CSV file containing screw specifications.
        """
        self.specifications = self._load_specifications(specifications_file)
    
    def _load_specifications(self, file_path: str) -> Dict[str, Dict[str, float]]:
        """
        Load screw specifications from a CSV file.
        
        Args:
            file_path (str): Path to the CSV file.
            
        Returns:
            Dict[str, Dict[str, float]]: Dictionary containing screw specifications.
            
        Raises:
            FileNotFoundError: If the specifications file is not found.
            ValueError: If the specifications file is malformed.
        """
        specifications = {}
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        screw_type = row['type']
                        specifications[screw_type] = {
                            'weight_per_unit': float(row['weight_per_unit']),
                            'quantity_per_package': int(row['quantity_per_package'])
                        }
                    except (KeyError, ValueError) as e:
                        raise ValueError(f"Malformed data in specifications file: {e}")
        except FileNotFoundError:
            raise FileNotFoundError(f"Specifications file not found: {file_path}")
        return specifications
    
    def calculate_total(self, order: Dict[str, int]) -> Tuple[float, int]:
        """
        Calculate the total weight and quantity of screws based on the order.
        
        Args:
            order (Dict[str, int]): Dictionary with screw types as keys and quantities as values.
            
        Returns:
            Tuple[float, int]: Total weight in grams and total quantity of screws.
            
        Raises:
            ValueError: If a screw type in the order is not found in specifications.
        """
        total_weight = 0.0
        total_quantity = 0
        
        for screw_type, quantity in order.items():
            if screw_type not in self.specifications:
                raise ValueError(f"Screw type '{screw_type}' not found in specifications")
            
            spec = self.specifications[screw_type]
            total_weight += quantity * spec['weight_per_unit']
            total_quantity += quantity
        
        return (total_weight, total_quantity)

def main():
    try:
        # Example usage
        calculator = ScrewCalculator('screw_specifications.csv')
        
        # Example order: {'type1': 100, 'type2': 50}
        order = {
            'M3x10': 100,
            'M4x12': 50
        }
        
        total_weight, total_quantity = calculator.calculate_total(order)
        print(f"Total weight: {total_weight:.2f} grams")
        print(f"Total quantity: {total_quantity} screws")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
