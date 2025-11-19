"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: Write a Python script that calculates the potential property loss reduction when installing fire sprinklers, based on statistics from Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_76ad361edb0369b8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import sys
from typing import Dict, Union, Optional

# Configuration file path (can be modified for different environments)
CONFIG_FILE = "sprinkler_config.json"

class SprinklerCalculator:
    """
    A class to calculate potential property loss reduction when installing fire sprinklers.
    Uses statistics from Independence Fire Sprinkler Company.
    """
    
    def __init__(self, config_file: str = CONFIG_FILE):
        """
        Initialize the calculator with configuration data.
        
        Args:
            config_file: Path to JSON configuration file containing statistics
        """
        try:
            with open(config_file, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            print(f"Error: Configuration file {config_file} not found.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in configuration file {config_file}.")
            sys.exit(1)
        except Exception as e:
            print(f"Error loading configuration: {str(e)}")
            sys.exit(1)
            
        # Validate required configuration fields
        required_fields = ['average_loss_without_sprinklers', 
                          'average_loss_with_sprinklers',
                          'reduction_factors']
        for field in required_fields:
            if field not in self.config:
                print(f"Error: Missing required field '{field}' in configuration.")
                sys.exit(1)
    
    def calculate_loss_reduction(self, 
                               property_value: float, 
                               property_type: Optional[str] = None) -> Dict[str, Union[float, str]]:
        """
        Calculate potential loss reduction for a property.
        
        Args:
            property_value: Total value of the property
            property_type: Optional property type for specific reduction factors
            
        Returns:
            Dictionary containing:
            - original_loss: Estimated loss without sprinklers
            - reduced_loss: Estimated loss with sprinklers
            - reduction_amount: Absolute reduction amount
            - reduction_percentage: Percentage reduction
            - message: Human-readable result
        """
        if property_value <= 0:
            raise ValueError("Property value must be positive.")
            
        try:
            # Get base reduction factors
            avg_without = self.config['average_loss_without_sprinklers']
            avg_with = self.config['average_loss_with_sprinklers']
            
            # Calculate base reduction
            original_loss = property_value * avg_without
            reduced_loss = property_value * avg_with
            reduction_amount = original_loss - reduced_loss
            reduction_percentage = (reduction_amount / original_loss) * 100
            
            # Apply property type specific factor if provided
            if property_type and property_type in self.config['reduction_factors']:
                factor = self.config['reduction_factors'][property_type]
                reduced_loss *= factor
                reduction_amount = original_loss - reduced_loss
                reduction_percentage = (reduction_amount / original_loss) * 100
            
            return {
                'original_loss': round(original_loss, 2),
                'reduced_loss': round(reduced_loss, 2),
                'reduction_amount': round(reduction_amount, 2),
                'reduction_percentage': round(reduction_percentage, 2),
                'message': (f"Installing sprinklers could reduce potential loss from "
                          f"${original_loss:,.2f} to ${reduced_loss:,.2f} "
                          f"({reduction_percentage:.2f}% reduction)")
            }
            
        except Exception as e:
            raise RuntimeError(f"Error calculating loss reduction: {str(e)}")

def main():
    """Main function to demonstrate the calculator."""
    try:
        calculator = SprinklerCalculator()
        
        # Example usage
        property_value = 1000000  # $1,000,000 property
        property_type = "office"  # Optional property type
        
        result = calculator.calculate_loss_reduction(property_value, property_type)
        print(result['message'])
        
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
