"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lagraveusenormande.fr
Prompt: Create a script to automate the generation of personalized door plaques and mailbox plaques, including engraving text and selecting materials, based on the offerings of "La Graveuse Normande."
Generated: DETERMINISTIC_f5e7ef5b406a7d38
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

class PlaqueOrder:
    """
    A class representing an order for a door or mailbox plaque.
    """
    def __init__(self, customer_name, plaque_type, engraving_text, material):
        """
        Initializes the PlaqueOrder object.
        
        :param customer_name: Name of the customer placing the order.
        :param plaque_type: Type of plaque ('door' or 'mailbox').
        :param engraving_text: Text to be engraved on the plaque.
        :param material: Material for the plaque (e.g., 'wood', 'metal', 'plastic').
        """
        self.customer_name = customer_name
        self.plaque_type = plaque_type.lower()
        self.engraving_text = engraving_text
        self.material = material.lower()
        self.validate_inputs()
    
    def validate_inputs(self):
        """
        Validates the input data for the plaque order.
        """
        valid_plaque_types = ['door', 'mailbox']
        valid_materials = ['wood', 'metal', 'plastic']
        
        if self.plaque_type not in valid_plaque_types:
            raise ValueError(f"Invalid plaque type: {self.plaque_type}. Must be 'door' or 'mailbox'.")
        
        if self.material not in valid_materials:
            raise ValueError(f"Invalid material: {self.material}. Must be one of {valid_materials}.")
        
        if not self.engraving_text:
            raise ValueError("Engraving text cannot be empty.")

    def generate_plaque_description(self):
        """
        Generates a string description of the plaque order.
        
        :return: Description of the plaque order as a string.
        """
        return (f"Plaque Type: {self.plaque_type.capitalize()}\n"
                f"Material: {self.material.capitalize()}\n"
                f"Engraving Text: {self.engraving_text}\n")


def save_order_to_file(order):
    """
    Saves the plaque order details to a file.
    
    :param order: The PlaqueOrder object containing order details.
    """
    directory = "orders"
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_name = f"{directory}/{order.customer_name.replace(' ', '_').lower()}_{order.plaque_type}_plaque.txt"
    try:
        with open(file_name, 'w') as file:
            file.write(f"Customer Name: {order.customer_name}\n")
            file.write(order.generate_plaque_description())
        print(f"Order saved successfully: {file_name}")
    except Exception as e:
        print(f"Error saving order to file: {e}")


def main():
    """
    Main function to handle user input and create plaque orders.
    """
    print("Welcome to La Graveuse Normande!")
    try:
        customer_name = input("Enter your name: ").strip()
        plaque_type = input("Enter plaque type ('door' or 'mailbox'): ").strip()
        engraving_text = input("Enter engraving text for the plaque: ").strip()
        material = input("Enter material for the plaque ('wood', 'metal', 'plastic'): ").strip()
        
        # Create a plaque order
        order = PlaqueOrder(customer_name, plaque_type, engraving_text, material)
        
        # Save the order to a file
        save_order_to_file(order)
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
