"""
Generated Code Metadata:
========================
Original URL: https://otoekspertiz.com.tr
Prompt: Write a code snippet to compare the features of different vehicle inspection packages (e.g., KB Paket, MM Paket, EKS Paket) offered by Computest Oto Ekspertiz and recommend the most suitable package based on user input.
Generated: DETERMINISTIC_d5d1ced4fd575c04
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import sys

# Define the vehicle inspection packages and their features
inspection_packages = {
    "KB Paket": {
        "features": ["Engine Check", "Transmission Check", "Brake System Check"],
        "price": 100
    },
    "MM Paket": {
        "features": ["Engine Check", "Transmission Check", "Brake System Check", "Suspension Check", "Interior Check"],
        "price": 150
    },
    "EKS Paket": {
        "features": ["Engine Check", "Transmission Check", "Brake System Check", "Suspension Check", "Interior Check", "Exterior Check", "Advanced Diagnostics"],
        "price": 200
    }
}

# Function to display package details
def display_packages(packages):
    print("\nAvailable Inspection Packages:")
    for package_name, details in packages.items():
        print(f"\n{package_name}:")
        print(f"  Features: {', '.join(details['features'])}")
        print(f"  Price: ${details['price']}")

# Function to recommend the most suitable package based on user input
def recommend_package(packages, user_needs, budget):
    suitable_packages = []
    for package_name, details in packages.items():
        # Check if all user needs are covered by the package features
        if all(need in details['features'] for need in user_needs):
            # Check if the package is within the user's budget
            if details['price'] <= budget:
                suitable_packages.append((package_name, details['price']))
    
    # Sort suitable packages by price (ascending)
    suitable_packages.sort(key=lambda x: x[1])
    
    if suitable_packages:
        print("\nRecommended Package(s):")
        for package_name, price in suitable_packages:
            print(f"  {package_name} - ${price}")
    else:
        print("\nNo suitable packages found within your budget and requirements.")

# Main function
def main():
    try:
        # Display available packages
        display_packages(inspection_packages)
        
        # Get user input for required features
        user_needs = input("\nEnter the features you need (comma-separated): ").strip().split(",")
        user_needs = [need.strip() for need in user_needs]
        
        # Get user input for budget
        budget = float(input("Enter your budget: ").strip())
        
        # Recommend the most suitable package
        recommend_package(inspection_packages, user_needs, budget)
    
    except ValueError:
        print("\nError: Invalid input. Please enter a valid budget.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)

# Entry point of the program
if __name__ == "__main__":
    main()
```
