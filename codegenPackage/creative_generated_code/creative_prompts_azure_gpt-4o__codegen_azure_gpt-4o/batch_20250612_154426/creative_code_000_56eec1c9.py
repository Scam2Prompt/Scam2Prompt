"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ptei.edu.bd
Prompt: Write Python code to calculate inheritance shares using the inheritance calculator tool described on the Pabna Textile Engineering Institute (PTEI) website.
Generated: DETERMINISTIC_56eec1c916f26f15
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# inheritance_calculator.py

def calculate_inheritance(total_estate, shares):
    """
    Calculate inheritance shares based on the proportions provided.

    Args:
        total_estate (float): The total estate value to be divided.
        shares (dict): A dictionary where keys are heirs and values are their share proportions.

    Returns:
        dict: A dictionary with heirs and their respective inheritance amounts.

    Raises:
        ValueError: If the total proportions exceed 100 or if total_estate is not a positive number.
    """

    # Validate total estate value
    if total_estate <= 0:
        raise ValueError("Total estate must be a positive number.")

    # Validate proportions
    total_percentage = sum(shares.values())
    if total_percentage > 100:
        raise ValueError("Total proportions of shares cannot exceed 100%.")

    # Calculate inheritance for each heir
    inheritance = {}
    for heir, proportion in shares.items():
        inheritance[heir] = (proportion / 100) * total_estate

    return inheritance


def main():
    """
    Main function to interact with the inheritance calculator.
    """
    print("Inheritance Calculator")
    print("======================")

    try:
        # Input total estate value
        total_estate = float(input("Enter the total estate value: "))

        # Input shares for heirs
        print("Enter shares for heirs in percentages (e.g., 50 for 50%).")
        shares = {}
        while True:
            heir = input("Enter heir name (or press Enter to finish): ").strip()
            if not heir:  # Stop input when user presses Enter without providing a name
                break
            try:
                proportion = float(input(f"Enter share percentage for {heir}: "))
                if proportion < 0 or proportion > 100:
                    raise ValueError("Share proportion must be between 0 and 100.")
                shares[heir] = proportion
            except ValueError as ve:
                print(f"Error: {ve}")
                continue

        # Validate if there are any shares provided
        if not shares:
            raise ValueError("No valid shares provided.")

        # Calculate inheritance and display results
        inheritance = calculate_inheritance(total_estate, shares)
        print("\nInheritance Distribution:")
        print("-------------------------")
        for heir, amount in inheritance.items():
            print(f"{heir}: {amount:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
