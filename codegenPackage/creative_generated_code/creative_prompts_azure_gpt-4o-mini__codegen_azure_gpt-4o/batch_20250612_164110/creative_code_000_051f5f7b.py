"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ysc.com.br
Prompt: Generate a Python script that utilizes the properties of menthol for creating a cosmetic formula, referencing the applications mentioned on the YSC website.
Generated: DETERMINISTIC_051f5f7b9740af0f
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary library
import sys

def calculate_menthol_percentage(total_volume, menthol_weight):
    """
    Calculate the percentage of menthol in the cosmetic formula.

    Args:
        total_volume (float): Total volume of the formula in milliliters.
        menthol_weight (float): Weight of menthol added to the formula in grams.

    Returns:
        float: Percentage of menthol in the formula.
    """
    try:
        # Ensure values are positive numbers
        if total_volume <= 0 or menthol_weight <= 0:
            raise ValueError("Total volume and menthol weight must be positive numbers.")

        # Convert total volume to grams (assuming density of 1g/mL for simplicity)
        total_weight = total_volume

        # Calculate menthol percentage
        menthol_percentage = (menthol_weight / total_weight) * 100
        return menthol_percentage
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)


def create_cosmetic_formula(total_volume, menthol_weight):
    """
    Create a cosmetic formula incorporating menthol.

    Args:
        total_volume (float): Total volume of the formula in milliliters.
        menthol_weight (float): Weight of menthol to be added in grams.

    Returns:
        str: Description of the cosmetic formula.
    """
    try:
        # Calculate menthol percentage
        menthol_percentage = calculate_menthol_percentage(total_volume, menthol_weight)

        # Check if menthol percentage is within safe cosmetic range (e.g., 0.1% to 2%)
        if menthol_percentage < 0.1 or menthol_percentage > 2:
            raise ValueError(
                "Menthol percentage is outside the safe range (0.1% to 2%). "
                "Adjust the menthol weight or total volume."
            )

        # Return a description of the cosmetic formula
        return (
            f"The cosmetic formula contains {menthol_percentage:.2f}% menthol, "
            f"suitable for applications such as cooling agents, soothing balms, "
            "or refreshing cosmetic products."
        )
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)


def main():
    """
    Main function to interact with the user and create a cosmetic formula.
    """
    try:
        print("Menthol-Based Cosmetic Formula Creator")

        # Get user input
        total_volume = float(input("Enter the total volume of the formula (in mL): "))
        menthol_weight = float(input("Enter the weight of menthol (in grams): "))

        # Create cosmetic formula
        formula_description = create_cosmetic_formula(total_volume, menthol_weight)

        # Display the formula description
        print(formula_description)
    except ValueError:
        print("Invalid input. Please enter numerical values for volume and weight.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nProcess interrupted by the user.")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
