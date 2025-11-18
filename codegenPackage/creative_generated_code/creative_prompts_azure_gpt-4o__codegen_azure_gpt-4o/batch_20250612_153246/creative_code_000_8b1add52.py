"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.oasishottubsep.com
Prompt: Write a Python script to create a pricing calculator for Jacuzzi® hot tubs, incorporating features like hydrotherapy jets, ergonomic seats, and energy-saving technology as described on the Oasis Hot Tubs website.
Generated: DETERMINISTIC_8b1add520ccb7ce6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def main():
    """
    Main function to handle user input and calculate the price of a Jacuzzi hot tub.
    """
    print("Welcome to the Jacuzzi Hot Tub Pricing Calculator!")
    print("Please select features for your hot tub:")
    
    # Initialize base price
    base_price = 5000  # Base price in USD for the hot tub
    
    # Features and their additional costs
    features = {
        "hydrotherapy_jets": 1000,  # Cost for hydrotherapy jets
        "ergonomic_seats": 750,    # Cost for ergonomic seats
        "energy_saving_tech": 800, # Cost for energy-saving technology
    }
    
    # User-selected features
    selected_features = []

    # Error handling for user input
    try:
        # Feature selection
        print("\nAvailable features:")
        for idx, feature in enumerate(features.keys(), start=1):
            print(f"{idx}. {feature.replace('_', ' ').title()} (${features[feature]} USD)")
        
        user_input = input(
            "\nEnter the numbers corresponding to the features you want (comma-separated, e.g., 1,3): "
        )
        selected_indices = user_input.split(",")

        # Validate and add features
        for idx in selected_indices:
            idx = idx.strip()  # Remove extra spaces
            if idx.isdigit() and 0 < int(idx) <= len(features):
                feature_key = list(features.keys())[int(idx) - 1]
                selected_features.append(feature_key)
            else:
                print(f"Invalid selection: {idx}. Please enter numbers between 1 and {len(features)}.")
                sys.exit(1)

        # Calculate total price
        total_price = base_price + sum(features[feature] for feature in selected_features)

        # Print selected features and total cost
        print("\nYour selected features:")
        for feature in selected_features:
            print(f"- {feature.replace('_', ' ').title()} (+${features[feature]} USD)")

        print(f"\nTotal Price: ${total_price} USD")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
