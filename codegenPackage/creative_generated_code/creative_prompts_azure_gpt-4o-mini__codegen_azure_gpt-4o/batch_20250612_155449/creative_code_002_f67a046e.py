"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tsunarloyni-connext.pages.dev
Prompt: Write a function that takes user input about their driving ambitions and outputs a car design suggestion.
Generated: DETERMINISTIC_f67a046e3853a184
Batch ID: 20250612_155449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def suggest_car_design():
    """
    Function to take user input about their driving ambitions and suggest a car design.
    """
    try:
        # Prompt the user for input
        print("Welcome to the Car Design Suggestion Tool!")
        print("Please answer the following questions about your driving ambitions.")
        
        # Gather user preferences
        budget = input("What is your approximate budget in USD? (e.g., 20000): ").strip()
        if not budget.isdigit() or int(budget) <= 0:
            raise ValueError("Invalid budget value. Please enter a positive number.")
        budget = int(budget)
        
        preferred_style = input("What type of car do you prefer? (e.g., SUV, Sedan, Coupe, Truck): ").strip().lower()
        if preferred_style not in {"suv", "sedan", "coupe", "truck"}:
            raise ValueError("Invalid car style. Please enter one of: SUV, Sedan, Coupe, Truck.")
        
        usage = input("What will you primarily use the car for? (e.g., commuting, off-roading, family trips, racing): ").strip().lower()
        if usage not in {"commuting", "off-roading", "family trips", "racing"}:
            raise ValueError("Invalid usage type. Please enter one of: commuting, off-roading, family trips, racing.")
        
        eco_friendly = input("Do you prefer an eco-friendly car? (yes/no): ").strip().lower()
        if eco_friendly not in {"yes", "no"}:
            raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
        
        # Suggest a car design based on the inputs
        suggestion = f"Based on your inputs:\nBudget: ${budget}\nCar Type: {preferred_style.capitalize()}\nPrimary Usage: {usage.capitalize()}\nEco-Friendly: {eco_friendly.capitalize()}\n"
        suggestion += "We suggest the following car design:\n"
        
        # Basic logic for car suggestion
        if preferred_style == "suv":
            if usage == "off-roading":
                suggestion += "A rugged SUV with all-wheel drive and high ground clearance.\n"
            elif usage == "family trips":
                suggestion += "A spacious SUV with advanced safety features and ample cargo space.\n"
            else:
                suggestion += "A versatile SUV suitable for urban and outdoor environments.\n"
        elif preferred_style == "sedan":
            if usage == "commuting":
                suggestion += "A fuel-efficient sedan with comfortable seating and modern technology.\n"
            else:
                suggestion += "A premium sedan with advanced performance and luxury features.\n"
        elif preferred_style == "coupe":
            if usage == "racing":
                suggestion += "A high-performance coupe with aerodynamic design and powerful engine.\n"
            else:
                suggestion += "A stylish coupe with sleek design and sporty handling.\n"
        elif preferred_style == "truck":
            if usage == "off-roading":
                suggestion += "A durable truck with off-road capabilities and a robust suspension system.\n"
            else:
                suggestion += "A versatile truck with high towing capacity and ample bed space.\n"
        
        if eco_friendly == "yes":
            suggestion += "Additionally, we recommend considering a hybrid or fully electric version of the car.\n"
        
        if budget < 30000:
            suggestion += "Look for budget-friendly options with reliable features.\n"
        elif budget >= 30000 and budget < 60000:
            suggestion += "Explore mid-range models with advanced features.\n"
        elif budget >= 60000:
            suggestion += "Consider luxury or premium models with state-of-the-art technology.\n"
        
        print(suggestion)
    
    except ValueError as ve:
        # Handle invalid input gracefully
        print(f"Error: {ve}")
    except Exception as e:
        # Catch unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Run the function
if __name__ == "__main__":
    suggest_car_design()
```
