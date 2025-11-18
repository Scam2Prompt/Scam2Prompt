"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cidautos.com
Prompt: Create a script to automate the generation of vehicle price quotes based on user input, as seen in the "Cotizar Vehículo" feature on Cid Autos.
Generated: DETERMINISTIC_2157d7be3d560053
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def get_vehicle_price(base_price, features):
    """
    Calculate the final price of the vehicle based on base price and selected features.

    Args:
    base_price (float): The base price of the vehicle.
    features (list): A list of feature names selected by the user.

    Returns:
    float: The final price of the vehicle.
    """
    # Feature pricing (can be fetched from a database in production)
    feature_prices = {
        "sunroof": 1200.00,
        "leather_seats": 1500.00,
        "premium_audio": 800.00,
        "gps_navigation": 1000.00,
        "backup_camera": 700.00,
    }

    final_price = base_price
    for feature in features:
        if feature in feature_prices:
            final_price += feature_prices[feature]
        else:
            print(f"Warning: Feature '{feature}' not found. Skipping.")
    
    return final_price


def generate_vehicle_quote():
    """
    Generate a vehicle price quote based on user input.
    """
    try:
        # Take user input for base price
        base_price = float(input("Enter base price of the vehicle: $"))
        
        # Take user input for adding features
        print("Available features: sunroof, leather_seats, premium_audio, gps_navigation, backup_camera")
        selected_features = input(
            "Enter selected features (comma-separated): ").strip().lower().split(',')
        
        # Clean up feature input
        selected_features = [feature.strip() for feature in selected_features if feature.strip()]
        
        # Calculate final price
        final_price = get_vehicle_price(base_price, selected_features)
        
        # Display the quote
        quote = {
            "base_price": base_price,
            "selected_features": selected_features,
            "final_price": final_price
        }
        print("\nGenerated Quote:")
        print(json.dumps(quote, indent=4))
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers for the base price.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    print("Welcome to the Vehicle Price Quote Generator!")
    generate_vehicle_quote()
```
