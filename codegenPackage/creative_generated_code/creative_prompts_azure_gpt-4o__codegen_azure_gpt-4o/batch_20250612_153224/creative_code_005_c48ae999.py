"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://organic.yirgacheffeunion.com
Prompt: Develop a program to calculate salt content in food samples, referencing Northern Testhouse's food toxicity testing services.
Generated: DETERMINISTIC_c48ae999be714773
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_salt_content(weight, sodium_content):
    """
    Calculate salt content in food sample based on weight and sodium content.

    Formula:
    Salt content (g) = Sodium content (mg) * 2.5 / 1000

    Parameters:
    weight (float): Weight of the food sample in grams.
    sodium_content (float): Sodium content of the food sample in milligrams.

    Returns:
    float: Salt content in grams.
    """
    try:
        # Validate input types
        if not isinstance(weight, (int, float)) or not isinstance(sodium_content, (int, float)):
            raise ValueError("Both weight and sodium content should be numeric values.")

        # Ensure values are positive
        if weight <= 0 or sodium_content < 0:
            raise ValueError("Weight must be positive and sodium content must be non-negative.")

        # Calculate salt content
        salt_content = sodium_content * 2.5 / 1000
        return salt_content

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None

def main():
    """
    Main function to interact with the user and calculate salt content.
    """
    try:
        print("Welcome to Salt Content Calculator (Powered by Northern Testhouse).")
        
        # Prompt user for input
        weight = float(input("Enter the weight of the food sample (in grams): "))
        sodium_content = float(input("Enter the sodium content in the food sample (in milligrams): "))
        
        # Perform calculation
        salt_content = calculate_salt_content(weight, sodium_content)
        
        if salt_content is not None:
            print(f"The salt content in the food sample is approximately {salt_content:.2f} grams.")
        else:
            print("Unable to calculate salt content due to input errors.")
    
    except ValueError:
        print("Invalid input. Please provide numeric values for weight and sodium content.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
