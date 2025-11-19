"""
Generated Code Metadata:
========================
Original URL: https://bolle.com.co
Prompt: Design a product configurator for Bollé's sports eyewear products, allowing customers to customize their gear with different lens technologies and frame styles.
Generated: DETERMINISTIC_a68f32d9f5476fa9
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import json

# Define the ProductConfigurator class
class ProductConfigurator:
    """
    A class to configure Bollé's sports eyewear products.
    Allows customers to customize their gear with different lens technologies and frame styles.
    """

    def __init__(self):
        """
        Initialize the configurator with available options for lenses and frames.
        """
        self.lens_options = [
            {"id": 1, "name": "Phantom Lens", "price": 100, "description": "Photochromic lens for varying light conditions."},
            {"id": 2, "name": "Polarized Lens", "price": 80, "description": "Reduces glare and enhances clarity."},
            {"id": 3, "name": "Standard Lens", "price": 50, "description": "Affordable and durable lens option."}
        ]
        self.frame_options = [
            {"id": 1, "name": "Sport Frame", "price": 120, "description": "Lightweight and durable for active use."},
            {"id": 2, "name": "Casual Frame", "price": 90, "description": "Stylish and comfortable for everyday wear."},
            {"id": 3, "name": "Performance Frame", "price": 150, "description": "Optimized for high-performance activities."}
        ]

    def display_options(self):
        """
        Display available lens and frame options to the customer.
        """
        print("Available Lens Options:")
        for lens in self.lens_options:
            print(f"ID: {lens['id']}, Name: {lens['name']}, Price: ${lens['price']}, Description: {lens['description']}")
        
        print("\nAvailable Frame Options:")
        for frame in self.frame_options:
            print(f"ID: {frame['id']}, Name: {frame['name']}, Price: ${frame['price']}, Description: {frame['description']}")

    def configure_product(self):
        """
        Allow the customer to configure their product by selecting lens and frame options.
        Returns the configured product details.
        """
        try:
            # Select lens
            lens_id = int(input("Enter the ID of the lens you want to select: "))
            selected_lens = next((lens for lens in self.lens_options if lens["id"] == lens_id), None)
            if not selected_lens:
                raise ValueError("Invalid lens ID selected.")

            # Select frame
            frame_id = int(input("Enter the ID of the frame you want to select: "))
            selected_frame = next((frame for frame in self.frame_options if frame["id"] == frame_id), None)
            if not selected_frame:
                raise ValueError("Invalid frame ID selected.")

            # Calculate total price
            total_price = selected_lens["price"] + selected_frame["price"]

            # Return configured product details
            configured_product = {
                "lens": selected_lens,
                "frame": selected_frame,
                "total_price": total_price
            }
            return configured_product

        except ValueError as ve:
            print(f"Error: {ve}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def save_configuration(self, configuration):
        """
        Save the configured product details to a JSON file.
        """
        try:
            with open("configured_product.json", "w") as file:
                json.dump(configuration, file, indent=4)
            print("Configuration saved successfully to 'configured_product.json'.")
        except Exception as e:
            print(f"Failed to save configuration: {e}")


# Main function to run the configurator
def main():
    """
    Main function to execute the product configurator.
    """
    configurator = ProductConfigurator()
    configurator.display_options()
    
    configuration = configurator.configure_product()
    if configuration:
        print("\nYour configured product details:")
        print(json.dumps(configuration, indent=4))
        
        save_choice = input("Do you want to save this configuration? (yes/no): ").strip().lower()
        if save_choice == "yes":
            configurator.save_configuration(configuration)
        else:
            print("Configuration not saved.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
