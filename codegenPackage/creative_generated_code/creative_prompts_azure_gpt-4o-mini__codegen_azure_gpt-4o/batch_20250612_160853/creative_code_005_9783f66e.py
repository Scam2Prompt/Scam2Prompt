"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kataskeui.gr
Prompt: How do I obtain an Energy Performance Certificate (ΠΕΑ) for a building, and what are the energy categories it can fall into?
Generated: DETERMINISTIC_9783f66efb5140a2
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python script that provides information on obtaining an Energy Performance Certificate (ΠΕΑ) and the energy categories. This is structured as a CLI tool.

```python
import sys

def get_energy_certificate_info():
    """
    Provides information on obtaining an Energy Performance Certificate (ΠΕΑ) for a building.
    Returns:
        str: Instructions on how to obtain the certificate.
    """
    return (
        "To obtain an Energy Performance Certificate (ΠΕΑ):\n"
        "1. Find a certified energy inspector accredited by the local authority.\n"
        "2. Provide all required building documentation (e.g., floor plans, construction permits).\n"
        "3. Schedule an on-site inspection with the energy inspector.\n"
        "4. The inspector will assess the building's energy efficiency through calculations and software.\n"
        "5. Pay the required fee for the assessment.\n"
        "6. Receive the ΠΕΑ with the building's energy classification."
    )

def get_energy_categories():
    """
    Provides a list of energy categories a building can fall into based on its energy efficiency.
    Returns:
        list: Energy categories.
    """
    return [
        "A+ (Highest Efficiency)",
        "A",
        "B+",
        "B",
        "C",
        "D",
        "E",
        "Z",
        "H (Lowest Efficiency)"
    ]

def main():
    """
    Main function to run the CLI tool.
    Provides options to view information about obtaining an Energy Performance Certificate and its energy categories.
    """
    try:
        print("Energy Performance Certificate (ΠΕΑ) Information Tool")
        print("1. How to obtain an Energy Performance Certificate (ΠΕΑ)")
        print("2. What are the energy categories?")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == "1":
            print("\nInstructions for obtaining an Energy Performance Certificate (ΠΕΑ):\n")
            print(get_energy_certificate_info())
        elif choice == "2":
            print("\nEnergy Categories:\n")
            for category in get_energy_categories():
                print(f"- {category}")
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
