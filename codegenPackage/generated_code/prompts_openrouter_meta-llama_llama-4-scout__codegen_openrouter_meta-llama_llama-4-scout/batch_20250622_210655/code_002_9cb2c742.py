"""
Generated Code Metadata:
========================
Original URL: https://www.purpledumpster.ca
Prompt: "Write a Python script to calculate the cost of renting a dumpster for a renovation project in Toronto, considering the dumpster size and type of waste."
Generated: DETERMINISTIC_9cb2c74278fa9981
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dumpster_rental_calculator.py

"""
Calculates the cost of renting a dumpster for a renovation project in Toronto.

The cost is based on the dumpster size and type of waste.
"""

# Define a dictionary to store dumpster sizes and their corresponding base costs
DUMPSTER_SIZES = {
    "10-yard": 350,
    "20-yard": 450,
    "30-yard": 550,
    "40-yard": 650
}

# Define a dictionary to store waste types and their corresponding costs per yard
WASTE_TYPES = {
    "construction": 50,
    "demolition": 75,
    "renovation": 25
}

def calculate_dumpster_rental_cost(dumpster_size, waste_type, rental_days):
    """
    Calculates the cost of renting a dumpster.

    Args:
        dumpster_size (str): The size of the dumpster (e.g., "10-yard", "20-yard", etc.).
        waste_type (str): The type of waste (e.g., "construction", "demolition", etc.).
        rental_days (int): The number of days the dumpster will be rented.

    Returns:
        float: The total cost of renting the dumpster.

    Raises:
        ValueError: If the dumpster size or waste type is not valid.
    """
    # Check if the dumpster size is valid
    if dumpster_size not in DUMPSTER_SIZES:
        raise ValueError(f"Invalid dumpster size: {dumpster_size}. Valid sizes: {list(DUMPSTER_SIZES.keys())}")

    # Check if the waste type is valid
    if waste_type not in WASTE_TYPES:
        raise ValueError(f"Invalid waste type: {waste_type}. Valid types: {list(WASTE_TYPES.keys())}")

    # Calculate the base cost of the dumpster rental
    base_cost = DUMPSTER_SIZES[dumpster_size]

    # Calculate the waste disposal cost
    waste_disposal_cost = WASTE_TYPES[waste_type] * rental_days

    # Calculate the daily rental cost (assuming $50 per day)
    daily_rental_cost = 50 * rental_days

    # Calculate the total cost
    total_cost = base_cost + waste_disposal_cost + daily_rental_cost

    # Add a Toronto-specific fee (assuming 10% of the total cost)
    toronto_fee = total_cost * 0.10
    total_cost += toronto_fee

    return total_cost

def main():
    try:
        dumpster_size = input("Enter the dumpster size (e.g., 10-yard, 20-yard, etc.): ")
        waste_type = input("Enter the type of waste (e.g., construction, demolition, etc.): ")
        rental_days = int(input("Enter the number of rental days: "))

        total_cost = calculate_dumpster_rental_cost(dumpster_size, waste_type, rental_days)
        print(f"The total cost of renting a {dumpster_size} dumpster for {rental_days} days with {waste_type} waste is: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
