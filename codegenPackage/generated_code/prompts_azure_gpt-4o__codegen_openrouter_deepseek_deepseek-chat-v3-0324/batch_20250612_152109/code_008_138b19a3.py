"""
Generated Code Metadata:
========================
Original URL: https://surffojotas.com
Prompt: Create a chatbot using Python that can assist customers with inquiries about flip-flop customization, material options, and bulk orders for events.
Generated: DETERMINISTIC_138b19a3ab6e39e4
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class FlipFlopChatbot:
    """
    A chatbot to assist customers with flip-flop customization, material options, and bulk orders.
    """
    
    def __init__(self):
        self.material_options = {
            "rubber": {
                "description": "Durable and waterproof, ideal for beachwear.",
                "colors": ["black", "white", "blue", "red", "green"],
                "price_per_pair": 15.99
            },
            "eva": {
                "description": "Lightweight and comfortable, great for everyday use.",
                "colors": ["black", "white", "pink", "gray", "navy"],
                "price_per_pair": 19.99
            },
            "leather": {
                "description": "Premium look and feel, suitable for casual outings.",
                "colors": ["brown", "black", "tan", "burgundy"],
                "price_per_pair": 29.99
            }
        }
        
        self.customization_options = {
            "logo_printing": {
                "description": "Add your logo or design to the flip-flops.",
                "price": 5.00
            },
            "text_printing": {
                "description": "Print custom text on the flip-flops.",
                "price": 3.00
            },
            "color_mixing": {
                "description": "Mix and match colors for straps and soles.",
                "price": 4.00
            }
        }
        
        self.bulk_discounts = {
            50: 0.05,    # 5% discount for 50+ pairs
            100: 0.10,   # 10% discount for 100+ pairs
            200: 0.15    # 15% discount for 200+ pairs
        }
        
        self.greetings = [
            "Hello! How can I assist you with your flip-flop needs today?",
            "Hi there! What can I help you with regarding flip-flops?",
            "Welcome! Are you looking to customize flip-flops or place a bulk order?"
        ]
        
        self.farewells = [
            "Thank you for your inquiry! Have a great day!",
            "We appreciate your interest! Feel free to come back anytime.",
            "Goodbye! Hope to assist you again soon."
        ]
    
    def get_material_info(self, material: str) -> Optional[Dict]:
        """
        Retrieve information about a specific material.
        
        Args:
            material: The material to query (rubber, eva, leather).
            
        Returns:
            Dict containing material details or None if not found.
        """
        return self.material_options.get(material.lower())
    
    def list_materials(self) -> List[str]:
        """
        List all available materials.
        
        Returns:
            List of material names.
        """
        return list(self.material_options.keys())
    
    def get_customization_info(self, option: str) -> Optional[Dict]:
        """
        Retrieve information about a customization option.
        
        Args:
            option: The customization option to query.
            
        Returns:
            Dict containing customization details or None if not found.
        """
        return self.customization_options.get(option.lower())
    
    def list_customizations(self) -> List[str]:
        """
        List all available customization options.
        
        Returns:
            List of customization option names.
        """
        return list(self.customization_options.keys())
    
    def calculate_bulk_price(self, quantity: int, material: str) -> float:
        """
        Calculate the total price for a bulk order with applicable discounts.
        
        Args:
            quantity: Number of pairs ordered.
            material: The material selected.
            
        Returns:
            Total price after applying discounts.
            
        Raises:
            ValueError: If material is not found or quantity is invalid.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
            
        material_info = self.get_material_info(material)
        if not material_info:
            raise ValueError(f"Material '{material}' not found.")
            
        base_price = material_info["price_per_pair"] * quantity
        
        # Apply the highest applicable discount
        discount = 0.0
        for threshold, disc in sorted(self.bulk_discounts.items(), reverse=True):
            if quantity >= threshold:
                discount = disc
                break
                
        return base_price * (1 - discount)
    
    def generate_response(self, user_input: str) -> str:
        """
        Process user input and generate an appropriate response.
        
        Args:
            user_input: The user's message.
            
        Returns:
            The chatbot's response.
        """
        input_lower = user_input.lower()
        
        # Greetings
        if any(word in input_lower for word in ["hi", "hello", "hey"]):
            return self.greetings[0]
            
        # Material inquiries
        if "material" in input_lower or "materials" in input_lower:
            if "list" in input_lower or "what" in input_lower or "which" in input_lower:
                materials = ", ".join(self.list_materials())
                return f"We offer the following materials: {materials}. Would you like details about any specific one?"
            
            for material in self.list_materials():
                if material in input_lower:
                    info = self.get_material_info(material)
                    colors = ", ".join(info["colors"])
                    return (f"Our {material} flip-flops are {info['description']} "
                           f"Available colors: {colors}. Price: ${info['price_per_pair']} per pair.")
                    
        # Customization inquiries
        if "custom" in input_lower or "personalize" in input_lower:
            if "list" in input_lower or "what" in input_lower or "which" in input_lower:
                customizations = ", ".join(self.list_customizations())
                return f"We offer these customizations: {customizations}. Would you like details about any?"
            
            for option in self.list_customizations():
                if option.replace("_", " ") in input_lower:
                    info = self.get_customization_info(option)
                    return (f"{option.replace('_', ' ').title()}: {info['description']} "
                           f"Additional cost: ${info['price']} per pair.")
                    
        # Bulk order inquiries
        if "bulk" in input_lower or "event" in input_lower or "quantity" in input_lower:
            if "price" in input_lower or "cost" in input_lower or "how much" in input_lower:
                try:
                    # Extract quantity and material from input
                    words = input_lower.split()
                    quantity = next((int(word) for word in words if word.isdigit()), None)
                    material = next((word for word in words if word in self.list_materials()), None)
                    
                    if quantity and material:
                        total = self.calculate_bulk_price(quantity, material)
                        return (f"For {quantity} pairs of {material} flip-flops, "
                               f"the total would be ${total:.2f} (including bulk discount).")
                    else:
                        return ("For bulk pricing, please specify quantity and material. "
                               "Example: 'Price for 100 rubber flip-flops'")
                except ValueError as e:
                    return f"Sorry, I couldn't process that request. {str(e)}"
            
        # Farewells
        if any(word in input_lower for word in ["bye", "goodbye", "thanks", "thank you"]):
            return self.farewells[0]
            
        # Default response
        return ("I can help with material options, customizations, or bulk orders. "
                "What would you like to know about?")

def main():
    """
    Run the chatbot in interactive mode.
    """
    chatbot = FlipFlopChatbot()
    print(chatbot.greetings[0])
    
    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
                
            if user_input.lower() in ["exit", "quit"]:
                print(chatbot.farewells[0])
                break
                
            response = chatbot.generate_response(user_input)
            print("Bot:", response)
            
        except KeyboardInterrupt:
            print("\n" + chatbot.farewells[0])
            break
        except Exception as e:
            print("Bot: Sorry, I encountered an error. Please try again.")
            if __debug__:
                print(f"[Debug] Error: {e}")

if __name__ == "__main__":
    main()
```
