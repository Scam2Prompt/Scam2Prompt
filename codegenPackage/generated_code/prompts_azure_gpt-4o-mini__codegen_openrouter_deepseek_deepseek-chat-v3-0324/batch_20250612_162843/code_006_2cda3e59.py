"""
Generated Code Metadata:
========================
Original URL: https://anywhere-adventure.com
Prompt: Write a script to automate the process of generating quotes for tailored travel packages, specifically for adventure sports and wildlife safaris in Kenya.
Generated: DETERMINISTIC_2cda3e59ad14f913
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional, Union

class TravelPackage:
    """Represents a travel package with adventure sports or wildlife safari options."""
    
    def __init__(self, name: str, base_price: float, activities: List[str], duration_days: int):
        """
        Initialize a travel package.
        
        Args:
            name: Name of the package.
            base_price: Base price in USD.
            activities: List of activities included.
            duration_days: Duration of the package in days.
        """
        self.name = name
        self.base_price = base_price
        self.activities = activities
        self.duration_days = duration_days
    
    def calculate_total_price(self, num_people: int, discount: float = 0.0) -> float:
        """
        Calculate the total price for the package.
        
        Args:
            num_people: Number of people.
            discount: Discount percentage (0-1).
        
        Returns:
            Total price after applying discount.
        
        Raises:
            ValueError: If num_people <= 0 or discount < 0 or > 1.
        """
        if num_people <= 0:
            raise ValueError("Number of people must be positive.")
        if discount < 0 or discount > 1:
            raise ValueError("Discount must be between 0 and 1.")
        
        total = self.base_price * num_people
        return total * (1 - discount)

class QuoteGenerator:
    """Generates quotes for travel packages."""
    
    def __init__(self, packages: List[TravelPackage]):
        """
        Initialize the quote generator with available packages.
        
        Args:
            packages: List of TravelPackage objects.
        """
        self.packages = packages
    
    def generate_quote(
        self,
        package_name: str,
        num_people: int,
        discount: float = 0.0,
        start_date: Optional[str] = None
    ) -> Dict[str, Union[str, float, List[str]]]:
        """
        Generate a quote for a travel package.
        
        Args:
            package_name: Name of the package.
            num_people: Number of people.
            discount: Discount percentage (0-1).
            start_date: Optional start date in YYYY-MM-DD format.
        
        Returns:
            Dictionary containing quote details.
        
        Raises:
            ValueError: If package not found or invalid input.
        """
        package = next((p for p in self.packages if p.name == package_name), None)
        if not package:
            raise ValueError(f"Package '{package_name}' not found.")
        
        try:
            total_price = package.calculate_total_price(num_people, discount)
        except ValueError as e:
            raise ValueError(f"Invalid input: {str(e)}")
        
        quote = {
            "package": package.name,
            "base_price_per_person": package.base_price,
            "num_people": num_people,
            "duration_days": package.duration_days,
            "activities": package.activities,
            "discount": discount * 100,
            "total_price": total_price,
            "currency": "USD",
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        if start_date:
            try:
                datetime.strptime(start_date, "%Y-%m-%d")
                quote["start_date"] = start_date
            except ValueError:
                raise ValueError("Invalid start date format. Use YYYY-MM-DD.")
        
        return quote
    
    def save_quote_to_file(self, quote: Dict[str, Union[str, float, List[str]]], filename: str) -> None:
        """
        Save the quote to a JSON file.
        
        Args:
            quote: Quote dictionary.
            filename: Output filename.
        
        Raises:
            IOError: If file cannot be written.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(quote, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save quote: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Define available packages
    packages = [
        TravelPackage(
            "Maasai Mara Safari",
            1200.0,
            ["Game drives", "Bird watching", "Cultural visits"],
            5
        ),
        TravelPackage(
            "Diani Adventure",
            850.0,
            ["Scuba diving", "Snorkeling", "Skydiving"],
            4
        )
    ]
    
    # Initialize quote generator
    generator = QuoteGenerator(packages)
    
    try:
        # Generate a quote
        quote = generator.generate_quote(
            package_name="Maasai Mara Safari",
            num_people=4,
            discount=0.1,
            start_date="2023-12-15"
        )
        
        # Save to file
        generator.save_quote_to_file(quote, "travel_quote.json")
        print("Quote generated and saved successfully.")
        
    except ValueError as e:
        print(f"Error generating quote: {str(e)}")
    except IOError as e:
        print(f"Error saving quote: {str(e)}")
```
