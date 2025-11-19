"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Write a Python script to generate a quote for a poultry building cleaning and disinfection service, considering factors like building size and location in Aire sur l'Adour.
Generated: DETERMINISTIC_1af0bf476775daa2
Batch ID: 20250622_210655
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
from enum import Enum, auto
from typing import Optional


class CleaningLevel(Enum):
    """Enum representing different levels of cleaning intensity."""
    STANDARD = auto()
    DEEP = auto()
    INDUSTRIAL = auto()


@dataclass
class QuoteDetails:
    """Data class to hold quote details."""
    building_size: float  # in square meters
    location: str
    cleaning_level: CleaningLevel
    has_poultry: bool = True
    special_requests: Optional[str] = None


class QuoteCalculator:
    """Class to calculate cleaning service quotes."""
    
    # Price per square meter for each cleaning level (in EUR)
    PRICE_PER_SQM = {
        CleaningLevel.STANDARD: 0.50,
        CleaningLevel.DEEP: 0.75,
        CleaningLevel.INDUSTRIAL: 1.20
    }
    
    # Location multipliers
    LOCATION_MULTIPLIERS = {
        "Aire sur l'Adour": 1.0,
        "default": 1.2  # for other locations
    }
    
    # Additional charges
    POULTRY_SURCHARGE = 0.10  # 10% surcharge for poultry buildings
    MINIMUM_CHARGE = 100.00  # minimum charge in EUR
    
    def calculate_quote(self, details: QuoteDetails) -> float:
        """
        Calculate the total quote based on provided details.
        
        Args:
            details: QuoteDetails object containing service parameters
            
        Returns:
            float: Calculated total price in EUR
        """
        try:
            # Base calculation
            base_price = details.building_size * self.PRICE_PER_SQM[details.cleaning_level]
            
            # Apply location multiplier
            location_mult = self.LOCATION_MULTIPLIERS.get(
                details.location, 
                self.LOCATION_MULTIPLIERS["default"]
            )
            total = base_price * location_mult
            
            # Apply poultry surcharge if applicable
            if details.has_poultry:
                total *= (1 + self.POULTRY_SURCHARGE)
            
            # Ensure minimum charge
            total = max(total, self.MINIMUM_CHARGE)
            
            return round(total, 2)
        
        except Exception as e:
            raise ValueError(f"Error calculating quote: {str(e)}")


def get_user_input() -> QuoteDetails:
    """Collect user input for quote calculation."""
    try:
        print("Poultry Building Cleaning Service Quote Generator")
        print("------------------------------------------------")
        
        size = float(input("Enter building size in square meters: "))
        location = input("Enter location (default: Aire sur l'Adour): ") or "Aire sur l'Adour"
        
        print("\nSelect cleaning level:")
        for i, level in enumerate(CleaningLevel, 1):
            print(f"{i}. {level.name}")
        
        level_choice = int(input("Enter choice (1-3): "))
        cleaning_level = list(CleaningLevel)[level_choice - 1]
        
        has_poultry = input("Is this for a poultry building? (y/n): ").lower() == 'y'
        
        special_requests = input("Any special requests (leave empty if none): ")
        if not special_requests:
            special_requests = None
        
        return QuoteDetails(
            building_size=size,
            location=location,
            cleaning_level=cleaning_level,
            has_poultry=has_poultry,
            special_requests=special_requests
        )
    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")


def generate_quote(details: QuoteDetails) -> dict:
    """Generate a complete quote with all details."""
    calculator = QuoteCalculator()
    total = calculator.calculate_quote(details)
    
    quote = {
        "building_size": details.building_size,
        "location": details.location,
        "cleaning_level": details.cleaning_level.name,
        "has_poultry": details.has_poultry,
        "special_requests": details.special_requests,
        "total_price": total,
        "currency": "EUR"
    }
    
    return quote


def display_quote(quote: dict):
    """Display the quote in a user-friendly format."""
    print("\n=== QUOTE SUMMARY ===")
    print(f"Building Size: {quote['building_size']} sqm")
    print(f"Location: {quote['location']}")
    print(f"Cleaning Level: {quote['cleaning_level']}")
    print(f"Poultry Building: {'Yes' if quote['has_poultry'] else 'No'}")
    if quote['special_requests']:
        print(f"Special Requests: {quote['special_requests']}")
    print(f"\nTotal Price: {quote['total_price']} {quote['currency']}")


def save_quote_to_file(quote: dict, filename: str = "cleaning_quote.json"):
    """Save the quote to a JSON file."""
    try:
        with open(filename, 'w') as f:
            json.dump(quote, f, indent=4)
        print(f"\nQuote saved to {filename}")
    except Exception as e:
        print(f"Error saving quote: {str(e)}")


def main():
    """Main function to run the quote generator."""
    try:
        details = get_user_input()
        quote = generate_quote(details)
        display_quote(quote)
        
        save = input("\nWould you like to save this quote? (y/n): ").lower() == 'y'
        if save:
            filename = input("Enter filename (default: cleaning_quote.json): ") or "cleaning_quote.json"
            save_quote_to_file(quote, filename)
            
    except ValueError as e:
        print(f"\nError: {str(e)}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
