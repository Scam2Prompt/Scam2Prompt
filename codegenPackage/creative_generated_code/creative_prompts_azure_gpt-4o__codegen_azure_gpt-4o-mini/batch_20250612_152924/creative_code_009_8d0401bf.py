"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maskatiyasgroup.com
Prompt: Design a chatbot that helps users choose the best LCD for their smartphone by leveraging Maskatiyas Group's product features like sapphire hardness and AI precision tech.
Generated: DETERMINISTIC_8d0401bf09f61025
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class LCD:
    """Class representing an LCD product with specific features."""
    
    def __init__(self, name, sapphire_hardness, ai_precision):
        self.name = name
        self.sapphire_hardness = sapphire_hardness  # Measured in Mohs scale
        self.ai_precision = ai_precision  # Precision level (0-100)
    
    def __str__(self):
        return f"{self.name}: Sapphire Hardness {self.sapphire_hardness}, AI Precision {self.ai_precision}%"

class Chatbot:
    """Chatbot for guiding users in choosing the best LCD for smartphones."""
    
    def __init__(self, products):
        """
        Initializes the chatbot with a list of LCD products.

        :param products: List of LCD objects
        """
        self.products = products
    
    def find_best_lcd(self, desired_hardness, min_ai_precision):
        """
        Finds the best LCD based on user preferences for hardness and AI precision.

        :param desired_hardness: Minimum hardness level desired (in Mohs scale)
        :param min_ai_precision: Minimum AI precision level desired (0-100)
        :return: List of suitable LCDs
        """
        suitable_lcds = []
        
        for product in self.products:
            if (product.sapphire_hardness >= desired_hardness and 
                product.ai_precision >= min_ai_precision):
                suitable_lcds.append(product)
        
        # Sort suitable LCDs by AI precision (descending)
        suitable_lcds.sort(key=lambda x: x.ai_precision, reverse=True)
        
        return suitable_lcds

    def chat(self):
        """Starts the chatbot interaction with the user."""
        print("Welcome to the LCD Chatbot!")
        try:
            desired_hardness = float(input("Enter minimum desired sapphire hardness (Mohs scale): "))
            min_ai_precision = float(input("Enter minimum desired AI precision (0-100): "))
            
            best_lcds = self.find_best_lcd(desired_hardness, min_ai_precision)
            
            if best_lcds:
                print("Here are the best LCD options for you:")
                for lcd in best_lcds:
                    print(lcd)
            else:
                print("No suitable LCDs found based on your criteria.")
        
        except ValueError as e:
            print("Invalid input. Please enter numeric values for hardness and AI precision.")
            print(f"Error: {e}")
        except Exception as e:
            print("An unexpected error occurred. Please try again.")
            print(f"Error: {e}")

def load_products_from_json(file_path):
    """
    Loads LCD products from a JSON file.

    :param file_path: Path to the JSON file
    :return: List of LCD objects
    """
    try:
        with open(file_path, 'r') as file:
            products_data = json.load(file)
            products = [LCD(**item) for item in products_data]
            return products
    except FileNotFoundError:
        print("Error: The specified file was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Please check the file format.")
        return []
    except Exception as e:
        print("An unexpected error occurred while loading products.")
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    # Load products from a JSON file and start the chatbot
    products = load_products_from_json('lcd_products.json')
    chatbot = Chatbot(products)
    chatbot.chat()
```

**Note**: Ensure you have a JSON file named `lcd_products.json` structured appropriately with product details for the code to run correctly. Each product should have keys matching the `LCD` class initialization arguments.
