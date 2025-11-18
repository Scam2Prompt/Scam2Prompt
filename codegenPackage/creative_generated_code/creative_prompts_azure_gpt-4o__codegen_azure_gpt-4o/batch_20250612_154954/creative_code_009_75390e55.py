"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-official-k.blogspot.com
Prompt: Create a chatbot that helps users select a computer configuration based on specifications like those on Londritech's website, including gaming or office use cases.
Generated: DETERMINISTIC_75390e557c8206bf
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def get_computer_configuration(use_case, budget, preferred_brand=None):
    """
    Suggest a computer configuration based on user requirements.

    Args:
        use_case (str): The intended use case, e.g., 'gaming' or 'office'.
        budget (float): The budget in USD.
        preferred_brand (str, optional): Preferred computer brand.

    Returns:
        dict: Suggested computer configuration.
    """
    # Pre-defined configurations for demonstration purposes.
    configurations = [
        {
            "name": "Gaming Beast",
            "use_case": "gaming",
            "brand": "Alienware",
            "processor": "Intel Core i7",
            "ram": "16GB",
            "storage": "1TB SSD",
            "gpu": "NVIDIA RTX 3080",
            "price": 2500
        },
        {
            "name": "Office Master",
            "use_case": "office",
            "brand": "Dell",
            "processor": "Intel Core i5",
            "ram": "8GB",
            "storage": "512GB SSD",
            "gpu": "Integrated Graphics",
            "price": 1000
        },
        {
            "name": "Gaming Entry",
            "use_case": "gaming",
            "brand": "HP",
            "processor": "AMD Ryzen 5",
            "ram": "8GB",
            "storage": "1TB HDD",
            "gpu": "AMD RX 6600",
            "price": 1200
        },
        {
            "name": "Office Budget",
            "use_case": "office",
            "brand": "Acer",
            "processor": "Intel Core i3",
            "ram": "4GB",
            "storage": "256GB SSD",
            "gpu": "Integrated Graphics",
            "price": 500
        }
    ]

    # Filter configurations based on criteria.
    result = [
        config for config in configurations
        if config["use_case"] == use_case and config["price"] <= budget and
        (preferred_brand is None or config["brand"].lower() == preferred_brand.lower())
    ]

    if not result:
        return {"error": "No matching configuration found. Please adjust your criteria."}

    return result


def chatbot():
    """
    Launches the chatbot interface for computer configuration selection.
    """
    print("Welcome to the Computer Configurator Bot!")
    print("I can help you find the best computer configuration for your needs.\n")

    try:
        # Get user inputs
        use_case = input("What is your use case? (e.g., gaming, office): ").lower()
        budget = float(input("What is your budget? (in USD): "))
        preferred_brand = input("Do you have a preferred brand? (Press Enter to skip): ").strip()

        # Get configurations
        suggestions = get_computer_configuration(use_case, budget, preferred_brand)

        # Display results
        if "error" in suggestions:
            print(suggestions["error"])
        else:
            print("\nHere are the suggested configurations for you:")
            print(json.dumps(suggestions, indent=4))
    except ValueError:
        print("Invalid input. Please provide valid numeric values for budget.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    chatbot()
```
