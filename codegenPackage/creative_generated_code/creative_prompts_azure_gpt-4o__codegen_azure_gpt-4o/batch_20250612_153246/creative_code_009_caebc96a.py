"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mctsummit.org
Prompt: Create a script to manage sponsorship packages (Silver, Bronze, Gold) for the MCT Summit, including features like pricing and benefits as described on the website.
Generated: DETERMINISTIC_caebc96a62813354
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
A Python script to manage sponsorship packages for the MCT Summit.
The script allows users to view sponsorship options, pricing, and associated benefits.
Includes proper error handling and follows best practices.

Author: Expert Programmer
"""

# Constants for sponsorship packages
SPONSORSHIP_PACKAGES = {
    "Silver": {
        "price": 5000,  # USD
        "benefits": [
            "Logo on event website",
            "Social media mention",
            "Small booth at the event",
        ],
    },
    "Bronze": {
        "price": 3000,  # USD
        "benefits": [
            "Logo on event website",
            "Social media mention",
        ],
    },
    "Gold": {
        "price": 10000,  # USD
        "benefits": [
            "Prominent logo placement on event website",
            "Dedicated social media campaign",
            "Large booth at the event",
            "Speaking opportunity during the keynote",
        ],
    },
}

def list_sponsorship_packages():
    """
    Display available sponsorship packages, their pricing, and benefits.
    """
    print("Available Sponsorship Packages:")
    for package_name, details in SPONSORSHIP_PACKAGES.items():
        print(f"\nPackage: {package_name}")
        print(f"Price: ${details['price']}")
        print("Benefits:")
        for benefit in details["benefits"]:
            print(f"- {benefit}")

def get_package_details(package_name):
    """
    Get details of a specific sponsorship package.
    
    Args:
        package_name (str): Name of the sponsorship package to retrieve.
    
    Returns:
        dict: Details of the sponsorship package if found, else None.
    """
    package_name = package_name.capitalize()  # Ensure proper capitalization
    return SPONSORSHIP_PACKAGES.get(package_name)

def main():
    """
    Main function to drive the script. Handles user interaction.
    """
    print("Welcome to the MCT Summit Sponsorship Management System!")
    
    while True:
        print("\nMenu:")
        print("1. List all sponsorship packages")
        print("2. Get details of a specific package")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice (1/2/3): "))
            
            if choice == 1:
                list_sponsorship_packages()
            elif choice == 2:
                package_name = input("Enter the name of the sponsorship package (Silver/Bronze/Gold): ")
                package_details = get_package_details(package_name)
                
                if package_details:
                    print(f"\nPackage: {package_name.capitalize()}")
                    print(f"Price: ${package_details['price']}")
                    print("Benefits:")
                    for benefit in package_details["benefits"]:
                        print(f"- {benefit}")
                else:
                    print("Error: Invalid package name. Please choose from Silver, Bronze, or Gold.")
            elif choice == 3:
                print("Thank you for using the MCT Summit Sponsorship Management System. Goodbye!")
                break
            else:
                print("Error: Invalid choice. Please select a valid option.")
        except ValueError:
            print("Error: Please enter a valid number.")

# Entry point for the script
if __name__ == "__main__":
    main()
```
