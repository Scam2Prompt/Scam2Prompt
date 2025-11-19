"""
Generated Code Metadata:
========================
Original URL: https://kataskeui.gr
Prompt: How can I obtain a building permit in Greece, and what steps are involved in the approval of small-scale works?
Generated: DETERMINISTIC_9d7657a528519a23
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides information on obtaining a building permit in Greece and the steps involved in the approval of small-scale works.
It uses a simple command-line interface to guide the user through the process.
"""

def get_building_permit_info():
    """
    Provides general information on obtaining a building permit in Greece.
    """
    info = """
    To obtain a building permit in Greece, follow these steps:
    1. Consult with a licensed architect or civil engineer to prepare the necessary plans and documents.
    2. Submit the required documents to the local urban planning office (Poliodomiki Ypiresia).
    3. Pay the applicable fees.
    4. Wait for the review and approval process, which may involve inspections and compliance checks.
    5. Once approved, you will receive the building permit.

    Note: The exact requirements may vary depending on the type and location of the construction.
    """
    return info


def get_small_scale_works_approval_info():
    """
    Provides information on the approval process for small-scale works in Greece.
    """
    info = """
    For small-scale works in Greece, the approval process typically involves:
    1. Preparing a simplified set of plans and documents (e.g., site plan, description of works).
    2. Submitting the documents to the local urban planning office or municipality.
    3. Paying the applicable fees.
    4. Receiving approval, which is usually faster than for larger projects.

    Examples of small-scale works include:
    - Minor renovations
    - Fencing
    - Installation of solar panels
    - Small extensions or modifications

    Note: Always consult with a professional to ensure compliance with local regulations.
    """
    return info


def main():
    """
    Main function to interact with the user and provide information.
    """
    print("Welcome to the Building Permit Information System for Greece!")
    print("Please select an option:")
    print("1. How to obtain a building permit in Greece")
    print("2. Steps involved in the approval of small-scale works")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice (1/2/3): "))
        if choice == 1:
            print(get_building_permit_info())
        elif choice == 2:
            print(get_small_scale_works_approval_info())
        elif choice == 3:
            print("Thank you for using the system. Goodbye!")
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
    except ValueError:
        print("Error: Please enter a valid number (1, 2, or 3).")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
