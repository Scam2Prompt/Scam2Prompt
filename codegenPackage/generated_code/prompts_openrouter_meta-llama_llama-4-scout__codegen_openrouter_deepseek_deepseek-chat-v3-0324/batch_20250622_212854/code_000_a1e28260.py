"""
Generated Code Metadata:
========================
Original URL: https://jaguarlandroverjakarta.com
Prompt: Write a Python script to simulate a car loan calculator for Jaguar Land Rover models, considering the promo and price list information from the Jaguar Land Rover Jakarta website.
Generated: DETERMINISTIC_a1e28260de29edbd
Batch ID: 20250622_212854
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
from typing import Dict, List, Optional

@dataclass
class CarModel:
    """Represents a car model with its details."""
    name: str
    base_price: float
    promo_rate: Optional[float] = None
    promo_duration: Optional[int] = None  # in months

class CarLoanCalculator:
    """Simulates a car loan calculator for Jaguar Land Rover models."""
    
    def __init__(self, models_data: Dict[str, Dict]):
        """Initialize the calculator with car models data.
        
        Args:
            models_data: Dictionary containing car models information.
                        Expected format:
                        {
                            "model_name": {
                                "base_price": float,
                                "promo_rate": Optional[float],
                                "promo_duration": Optional[int]
                            }
                        }
        """
        self.models: Dict[str, CarModel] = {}
        for name, details in models_data.items():
            self.models[name] = CarModel(
                name=name,
                base_price=details["base_price"],
                promo_rate=details.get("promo_rate"),
                promo_duration=details.get("promo_duration")
            )
    
    def calculate_monthly_payment(
        self,
        model_name: str,
        down_payment: float,
        loan_duration: int,
        interest_rate: float
    ) -> float:
        """Calculate monthly payment for a car loan.
        
        Args:
            model_name: Name of the car model.
            down_payment: Down payment amount.
            loan_duration: Loan duration in months.
            interest_rate: Annual interest rate (e.g., 0.05 for 5%).
            
        Returns:
            Monthly payment amount.
            
        Raises:
            ValueError: If model not found or invalid parameters provided.
        """
        if model_name not in self.models:
            raise ValueError(f"Model '{model_name}' not found.")
        
        model = self.models[model_name]
        if down_payment < 0 or loan_duration <= 0 or interest_rate < 0:
            raise ValueError("Invalid loan parameters.")
        
        loan_amount = model.base_price - down_payment
        if loan_amount <= 0:
            raise ValueError("Down payment must be less than car price.")
        
        # Apply promo rate if applicable
        if model.promo_rate is not None and loan_duration <= model.promo_duration:
            interest_rate = model.promo_rate
        
        monthly_rate = interest_rate / 12
        monthly_payment = (loan_amount * monthly_rate) / (1 - (1 + monthly_rate) ** -loan_duration)
        
        return round(monthly_payment, 2)
    
    def get_available_models(self) -> List[str]:
        """Return list of available car models."""
        return list(self.models.keys())
    
    def get_model_details(self, model_name: str) -> Dict:
        """Get details of a specific car model.
        
        Args:
            model_name: Name of the car model.
            
        Returns:
            Dictionary with model details.
            
        Raises:
            ValueError: If model not found.
        """
        if model_name not in self.models:
            raise ValueError(f"Model '{model_name}' not found.")
        
        model = self.models[model_name]
        return {
            "name": model.name,
            "base_price": model.base_price,
            "promo_rate": model.promo_rate,
            "promo_duration": model.promo_duration
        }

def load_models_from_json(file_path: str) -> Dict:
    """Load car models data from JSON file.
    
    Args:
        file_path: Path to JSON file.
        
    Returns:
        Dictionary containing car models data.
        
    Raises:
        FileNotFoundError: If file doesn't exist.
        json.JSONDecodeError: If file contains invalid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise json.JSONDecodeError("Invalid JSON format in file.", file_path, 0)

def main():
    """Main function to demonstrate the car loan calculator."""
    try:
        # Load models data (in a real app, this would come from a database or API)
        models_data = {
            "Jaguar F-PACE": {
                "base_price": 1500000000,
                "promo_rate": 0.03,
                "promo_duration": 12
            },
            "Range Rover Evoque": {
                "base_price": 1200000000,
                "promo_rate": 0.025,
                "promo_duration": 24
            },
            "Land Rover Defender": {
                "base_price": 2000000000,
                "promo_rate": None,
                "promo_duration": None
            }
        }
        
        calculator = CarLoanCalculator(models_data)
        
        print("Available models:")
        for model in calculator.get_available_models():
            print(f"- {model}")
        
        model_name = input("\nEnter model name: ")
        down_payment = float(input("Enter down payment amount: "))
        loan_duration = int(input("Enter loan duration (months): "))
        interest_rate = float(input("Enter annual interest rate (e.g., 0.05 for 5%): "))
        
        monthly_payment = calculator.calculate_monthly_payment(
            model_name, down_payment, loan_duration, interest_rate
        )
        
        print(f"\nMonthly payment for {model_name}: IDR {monthly_payment:,.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
