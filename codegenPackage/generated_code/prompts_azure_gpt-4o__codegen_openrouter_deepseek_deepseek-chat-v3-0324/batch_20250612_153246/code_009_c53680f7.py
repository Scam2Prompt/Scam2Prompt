"""
Generated Code Metadata:
========================
Original URL: https://duct-split.com
Prompt: Develop a Python program to calculate the cooling area coverage for Gree duct split systems based on their BTU rating, using models like "Gree GU18T/AK(E)" and "Gree GU60T/AKa" as examples.
Generated: DETERMINISTIC_c53680f74c9c5557
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Gree Duct Split System Cooling Area Calculator

This program calculates the recommended cooling area coverage in square meters
for Gree duct split systems based on their BTU rating. It uses standard BTU to
area conversion ratios with adjustments for typical room conditions.

Example models:
- Gree GU18T/AK(E): 18,000 BTU
- Gree GU60T/AKa: 60,000 BTU
"""

class GreeCoolingCalculator:
    """
    A class to calculate cooling area coverage for Gree duct split systems.
    
    Attributes:
        BTU_PER_SQM (int): Standard BTU per square meter for cooling (600 BTU/sqm)
        MODELS (dict): Dictionary of common Gree models and their BTU ratings
    """
    
    BTU_PER_SQM = 600  # Standard BTU per square meter for cooling
    
    MODELS = {
        "Gree GU18T/AK(E)": 18000,
        "Gree GU24T/AK(E)": 24000,
        "Gree GU30T/AK(E)": 30000,
        "Gree GU36T/AK(E)": 36000,
        "Gree GU48T/AK(E)": 48000,
        "Gree GU60T/AK(E)": 60000,
        "Gree GU60T/AKa": 60000,
    }
    
    @classmethod
    def calculate_coverage(cls, btu: int) -> float:
        """
        Calculate the cooling area coverage based on BTU rating.
        
        Args:
            btu (int): BTU rating of the unit
            
        Returns:
            float: Recommended coverage area in square meters
            
        Raises:
            ValueError: If BTU input is not positive
        """
        if btu <= 0:
            raise ValueError("BTU rating must be a positive number")
        return btu / cls.BTU_PER_SQM
    
    @classmethod
    def get_model_coverage(cls, model_name: str) -> float:
        """
        Get coverage area for a specific Gree model.
        
        Args:
            model_name (str): Name of the Gree model
            
        Returns:
            float: Recommended coverage area in square meters
            
        Raises:
            ValueError: If model is not found in the database
        """
        if model_name not in cls.MODELS:
            raise ValueError(f"Model '{model_name}' not found in database")
        return cls.calculate_coverage(cls.MODELS[model_name])
    
    @classmethod
    def list_models(cls) -> list:
        """
        List all available models in the database.
        
        Returns:
            list: List of available model names
        """
        return list(cls.MODELS.keys())


def main():
    """Main function to demonstrate the calculator functionality."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Gree Duct Split System Cooling Area Calculator"
    )
    parser.add_argument(
        "--btu", 
        type=int, 
        help="BTU rating to calculate coverage for"
    )
    parser.add_argument(
        "--model", 
        type=str, 
        help="Gree model name to calculate coverage for"
    )
    parser.add_argument(
        "--list-models", 
        action="store_true", 
        help="List all available models"
    )
    
    args = parser.parse_args()
    
    calculator = GreeCoolingCalculator()
    
    try:
        if args.list_models:
            print("Available Gree models:")
            for model in calculator.list_models():
                print(f"- {model}")
        elif args.model:
            coverage = calculator.get_model_coverage(args.model)
            print(f"Model {args.model} covers approximately {coverage:.2f} sqm")
        elif args.btu:
            coverage = calculator.calculate_coverage(args.btu)
            print(f"{args.btu} BTU covers approximately {coverage:.2f} sqm")
        else:
            parser.print_help()
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
