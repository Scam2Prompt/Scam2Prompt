"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurs.io
Prompt: Create a pricing calculator for AI-powered website services, inspired by the pricing model on Blurs.io.
Generated: DETERMINISTIC_eaccef7b719c8953
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PricingCalculator:
    """
    A class to calculate the pricing for AI-powered website services.
    The pricing model is inspired by Blurs.io.
    """

    def __init__(self, base_price, ai_service_price, additional_feature_price):
        """
        Initializes the pricing calculator with base prices.

        :param base_price: The base price for the website service
        :param ai_service_price: The additional price for AI-powered features
        :param additional_feature_price: The price for any additional features
        """
        self.base_price = base_price
        self.ai_service_price = ai_service_price
        self.additional_feature_price = additional_feature_price

    def calculate_total(self, include_ai=False, additional_features=0):
        """
        Calculates the total price based on selected services.

        :param include_ai: Boolean indicating whether to include AI services
        :param additional_features: Number of additional features chosen
        :return: Total price as a float
        """
        try:
            if additional_features < 0:
                raise ValueError("Number of additional features cannot be negative.")

            total_price = self.base_price
            if include_ai:
                total_price += self.ai_service_price
            
            total_price += additional_features * self.additional_feature_price
            
            return total_price

        except Exception as e:
            print(f"Error in price calculation: {e}")
            return None

    def display_pricing(self):
        """
        Displays the pricing breakdown for the user.
        """
        print("Pricing Information:")
        print(f"Base Price: ${self.base_price:.2f}")
        print(f"AI Service Price: ${self.ai_service_price:.2f}")
        print(f"Additional Feature Price: ${self.additional_feature_price:.2f} per feature")

        total_price_with_ai = self.calculate_total(include_ai=True, additional_features=0)
        print(f"Total Price with AI Service: ${total_price_with_ai:.2f}")

        total_price_without_ai = self.calculate_total(include_ai=False, additional_features=0)
        print(f"Total Price without AI Service: ${total_price_without_ai:.2f}")


# Example usage
if __name__ == "__main__":
    # Initialize the PricingCalculator with example prices
    base_price = 200.00  # Base price for the service
    ai_service_price = 100.00  # Price for AI-powered features
    additional_feature_price = 50.00  # Price for each additional feature

    calculator = PricingCalculator(base_price, ai_service_price, additional_feature_price)
    
    # Display the pricing information
    calculator.display_pricing()
    
    # Calculate a total price with specific options
    total = calculator.calculate_total(include_ai=True, additional_features=3)
    if total is not None:
        print(f"Total Price for AI Service with 3 additional features: ${total:.2f}")

    total = calculator.calculate_total(include_ai=False, additional_features=2)
    if total is not None:
        print(f"Total Price without AI Service with 2 additional features: ${total:.2f}")
```
