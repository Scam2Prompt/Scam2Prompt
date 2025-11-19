"""
Generated Code Metadata:
========================
Original URL: https://poocoinue.blogspot.com
Prompt: Create a promotional text for a social shoe sale on Calini Sapatos em Geral's online store.
Generated: DETERMINISTIC_25bad03f50eebd3d
Batch ID: 20250622_204841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PromotionalTextGenerator:
    """
    A class to generate promotional text for a shoe sale.
    """

    def __init__(self, store_name, sale_percentage, sale_duration):
        """
        Initializes the promotional text generator with store details.

        :param store_name: Name of the store
        :param sale_percentage: Discount percentage for the sale
        :param sale_duration: Duration of the sale
        """
        self.store_name = store_name
        self.sale_percentage = sale_percentage
        self.sale_duration = sale_duration

    def generate_promotional_text(self):
        """
        Generates a promotional text for the shoe sale.

        :return: A string containing the promotional text
        """
        try:
            # Validate input values
            if not isinstance(self.store_name, str) or not self.store_name:
                raise ValueError("Store name must be a non-empty string.")
            if not (isinstance(self.sale_percentage, (int, float)) and 0 <= self.sale_percentage <= 100):
                raise ValueError("Sale percentage must be a number between 0 and 100.")
            if not isinstance(self.sale_duration, str) or not self.sale_duration:
                raise ValueError("Sale duration must be a non-empty string.")

            # Create the promotional text
            promo_text = (
                f"🎉 Big Sale Alert at {self.store_name}! 🎉\n"
                f"Enjoy a fantastic {self.sale_percentage}% off on all shoes!\n"
                f"Don't miss out on this amazing offer, valid for {self.sale_duration}.\n"
                f"Shop now and step up your shoe game! 👟🥿"
            )
            return promo_text

        except ValueError as e:
            # Handle validation errors
            return f"Error generating promotional text: {e}"

        except Exception as e:
            # Handle any unexpected errors
            return f"An unexpected error occurred: {e}"


# Example usage
if __name__ == "__main__":
    # Create an instance of the promotional text generator
    promo_generator = PromotionalTextGenerator("Calini Sapatos em Geral", 30, "this weekend only")
    
    # Generate and print the promotional text
    promotional_text = promo_generator.generate_promotional_text()
    print(promotional_text)
```
