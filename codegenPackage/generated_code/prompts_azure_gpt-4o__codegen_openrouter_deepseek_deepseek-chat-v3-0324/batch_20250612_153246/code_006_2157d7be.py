"""
Generated Code Metadata:
========================
Original URL: https://cidautos.com
Prompt: Create a script to automate the generation of vehicle price quotes based on user input, as seen in the "Cotizar Vehículo" feature on Cid Autos.
Generated: DETERMINISTIC_2157d7be3d560053
Batch ID: 20250612_153246
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
from typing import Dict, Optional, Union

class VehicleQuoteGenerator:
    """
    A class to generate vehicle price quotes based on user input.
    """
    
    def __init__(self, base_price_data: Dict[str, Dict[str, float]]):
        """
        Initialize the quote generator with base price data.
        
        Args:
            base_price_data: Dictionary containing base prices for different vehicle models and options.
                            Format: {'model': {'option1': price, 'option2': price, ...}, ...}
        """
        self.base_price_data = base_price_data
        self.quote_history = []
        
    def validate_input(self, model: str, options: Dict[str, Union[str, int]]) -> bool:
        """
        Validate user input for model and options.
        
        Args:
            model: Vehicle model name
            options: Dictionary of selected options and their values
            
        Returns:
            bool: True if input is valid, False otherwise
        """
        if model not in self.base_price_data:
            return False
            
        for option, value in options.items():
            if option not in self.base_price_data[model]:
                return False
                
            # Validate option values (assuming numeric values)
            if not isinstance(value, (int, float)):
                return False
                
        return True
    
    def calculate_base_price(self, model: str) -> float:
        """
        Get base price for the specified model.
        
        Args:
            model: Vehicle model name
            
        Returns:
            float: Base price of the model
            
        Raises:
            ValueError: If model is not found
        """
        if model not in self.base_price_data:
            raise ValueError(f"Model '{model}' not found in price data")
        return self.base_price_data[model].get('base_price', 0)
    
    def calculate_options_price(self, model: str, options: Dict[str, Union[str, int]]) -> float:
        """
        Calculate total price for selected options.
        
        Args:
            model: Vehicle model name
            options: Dictionary of selected options and their values
            
        Returns:
            float: Total price of selected options
            
        Raises:
            ValueError: If model or options are invalid
        """
        if not self.validate_input(model, options):
            raise ValueError("Invalid model or options provided")
            
        total_options = 0.0
        for option, value in options.items():
            option_price = self.base_price_data[model][option]
            total_options += option_price * value
            
        return total_options
    
    def generate_quote(
        self,
        customer_name: str,
        model: str,
        options: Dict[str, Union[str, int]],
        discount: float = 0.0
    ) -> Dict[str, Union[str, float]]:
        """
        Generate a vehicle price quote.
        
        Args:
            customer_name: Name of the customer
            model: Vehicle model name
            options: Dictionary of selected options and their values
            discount: Optional discount percentage (0-100)
            
        Returns:
            Dict: Quote details including total price
            
        Raises:
            ValueError: If input validation fails
        """
        if not customer_name:
            raise ValueError("Customer name is required")
            
        if discount < 0 or discount > 100:
            raise ValueError("Discount must be between 0 and 100")
            
        base_price = self.calculate_base_price(model)
        options_price = self.calculate_options_price(model, options)
        
        subtotal = base_price + options_price
        discount_amount = subtotal * (discount / 100)
        total = subtotal - discount_amount
        
        quote = {
            'quote_id': f"Q-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'customer_name': customer_name,
            'model': model,
            'base_price': base_price,
            'options': options,
            'options_price': options_price,
            'discount_percentage': discount,
            'discount_amount': discount_amount,
            'total_price': total
        }
        
        self.quote_history.append(quote)
        return quote
    
    def save_quote_to_file(self, quote: Dict[str, Union[str, float]], filename: str) -> None:
        """
        Save quote to a JSON file.
        
        Args:
            quote: Quote dictionary to save
            filename: Output filename
            
        Raises:
            IOError: If file operation fails
        """
        try:
            with open(filename, 'w') as f:
                json.dump(quote, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save quote: {str(e)}")
    
    def get_quote_history(self) -> list:
        """
        Get history of all generated quotes.
        
        Returns:
            list: List of all generated quotes
        """
        return self.quote_history


# Example usage
if __name__ == "__main__":
    # Sample base price data (would normally come from a database or file)
    base_prices = {
        'Sedan': {
            'base_price': 25000.00,
            'color_premium': 500.00,
            'leather_seats': 1500.00,
            'tech_package': 2000.00,
            'warranty_years': 1000.00  # per year
        },
        'SUV': {
            'base_price': 35000.00,
            'color_premium': 600.00,
            'leather_seats': 1800.00,
            'tech_package': 2500.00,
            'warranty_years': 1200.00  # per year
        }
    }
    
    # Initialize quote generator
    quote_gen = VehicleQuoteGenerator(base_prices)
    
    # Sample customer input
    try:
        quote = quote_gen.generate_quote(
            customer_name="John Doe",
            model="SUV",
            options={
                'color_premium': 1,
                'leather_seats': 1,
                'tech_package': 1,
                'warranty_years': 3
            },
            discount=5.0
        )
        
        print("Generated Quote:")
        print(json.dumps(quote, indent=4))
        
        # Save to file
        quote_gen.save_quote_to_file(quote, "john_doe_quote.json")
        print("\nQuote saved to file.")
        
    except ValueError as e:
        print(f"Error generating quote: {str(e)}")
    except IOError as e:
        print(f"Error saving quote: {str(e)}")
```
