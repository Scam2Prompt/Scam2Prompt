"""
Generated Code Metadata:
========================
Original URL: https://localtravelcoupons.com
Prompt: Generate a code snippet for a travel booking application that allows users to customize travel packages based on their budget, similar to the services offered by Local Travel Coupons.
Generated: DETERMINISTIC_ef8773ea265bbaa2
Batch ID: 20250612_155248
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

class TravelPackage:
    """
    Represents a travel package with customizable options.
    """
    def __init__(self, name: str, base_price: float, options: Dict[str, float]):
        """
        Initialize a travel package.
        
        Args:
            name: Name of the package
            base_price: Base price without any options
            options: Dictionary of available options and their prices
        """
        self.name = name
        self.base_price = base_price
        self.options = options
        self.selected_options = {}

    def add_option(self, option_name: str) -> bool:
        """
        Add an option to the package.
        
        Args:
            option_name: Name of the option to add
            
        Returns:
            bool: True if option was added, False if option doesn't exist
        """
        if option_name in self.options:
            self.selected_options[option_name] = self.options[option_name]
            return True
        return False

    def remove_option(self, option_name: str) -> bool:
        """
        Remove an option from the package.
        
        Args:
            option_name: Name of the option to remove
            
        Returns:
            bool: True if option was removed, False if option wasn't selected
        """
        if option_name in self.selected_options:
            del self.selected_options[option_name]
            return True
        return False

    def calculate_total(self) -> float:
        """
        Calculate the total price of the package with selected options.
        
        Returns:
            float: Total price
        """
        return self.base_price + sum(self.selected_options.values())

    def get_available_options(self) -> List[str]:
        """
        Get list of available options not yet selected.
        
        Returns:
            List[str]: List of available option names
        """
        return [opt for opt in self.options if opt not in self.selected_options]

    def to_dict(self) -> Dict:
        """
        Convert package to dictionary for serialization.
        
        Returns:
            Dict: Dictionary representation of package
        """
        return {
            'name': self.name,
            'base_price': self.base_price,
            'selected_options': self.selected_options,
            'total_price': self.calculate_total()
        }


class TravelPackageManager:
    """
    Manages available travel packages and user selections.
    """
    def __init__(self):
        self.packages = {}

    def load_packages_from_file(self, file_path: str) -> bool:
        """
        Load travel packages from a JSON file.
        
        Args:
            file_path: Path to JSON file
            
        Returns:
            bool: True if loaded successfully, False otherwise
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                for pkg_data in data.get('packages', []):
                    self.packages[pkg_data['name']] = TravelPackage(
                        pkg_data['name'],
                        pkg_data['base_price'],
                        pkg_data['options']
                    )
            return True
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading packages: {e}")
            return False

    def get_package(self, name: str) -> Optional[TravelPackage]:
        """
        Get a package by name.
        
        Args:
            name: Name of the package
            
        Returns:
            Optional[TravelPackage]: Package if found, None otherwise
        """
        return self.packages.get(name)

    def get_packages_within_budget(self, budget: float) -> List[Dict]:
        """
        Get packages that can be customized within a given budget.
        
        Args:
            budget: Maximum budget
            
        Returns:
            List[Dict]: List of package info dictionaries within budget
        """
        result = []
        for pkg in self.packages.values():
            base_info = pkg.to_dict()
            if base_info['total_price'] <= budget:
                result.append(base_info)
        return result

    def customize_package(self, package_name: str, budget: float) -> Optional[Dict]:
        """
        Customize a package to fit within budget by selecting options.
        
        Args:
            package_name: Name of package to customize
            budget: Maximum budget
            
        Returns:
            Optional[Dict]: Customized package info if successful, None otherwise
        """
        pkg = self.get_package(package_name)
        if not pkg:
            return None

        # Start with base package
        current_total = pkg.base_price
        if current_total > budget:
            return None  # Can't even afford base package

        # Try adding options within budget
        for option in pkg.get_available_options():
            option_price = pkg.options[option]
            if current_total + option_price <= budget:
                pkg.add_option(option)
                current_total += option_price

        return pkg.to_dict()


# Example usage
if __name__ == "__main__":
    manager = TravelPackageManager()
    
    # Load packages from file (would typically be in a separate config file)
    sample_packages = {
        "packages": [
            {
                "name": "Weekend Getaway",
                "base_price": 299.99,
                "options": {
                    "breakfast": 15.99,
                    "airport_transfer": 25.50,
                    "city_tour": 45.00
                }
            },
            {
                "name": "Luxury Vacation",
                "base_price": 999.99,
                "options": {
                    "spa_access": 75.00,
                    "gourmet_dining": 120.00,
                    "private_transport": 150.00
                }
            }
        ]
    }
    
    # Save sample packages to temporary file for demo
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        json.dump(sample_packages, f)
        temp_file_path = f.name
    
    # Load packages and demonstrate functionality
    if manager.load_packages_from_file(temp_file_path):
        budget = 400.00
        affordable_packages = manager.get_packages_within_budget(budget)
        print(f"Packages within ${budget}:")
        for pkg in affordable_packages:
            print(f"- {pkg['name']}: ${pkg['total_price']:.2f}")
        
        # Customize a package
        customized = manager.customize_package("Weekend Getaway", 350.00)
        if customized:
            print("\nCustomized package:")
            print(f"Name: {customized['name']}")
            print(f"Base price: ${customized['base_price']:.2f}")
            print("Selected options:")
            for opt, price in customized['selected_options'].items():
                print(f"- {opt}: ${price:.2f}")
            print(f"Total: ${customized['total_price']:.2f}")
```
