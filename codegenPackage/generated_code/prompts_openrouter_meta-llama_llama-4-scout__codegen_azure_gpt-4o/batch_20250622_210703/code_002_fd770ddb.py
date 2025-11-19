"""
Generated Code Metadata:
========================
Original URL: https://strongtowerlaw.com
Prompt: Generate a code for a simple estate planning calculator for Louisiana residents, taking into account business successions and family planning.
Generated: DETERMINISTIC_fd770ddb0ede7d54
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def get_user_input(prompt, input_type=str):
    """
    Safely get user input and convert it to the specified type.
    :param prompt: The message to display to the user.
    :param input_type: The type to convert the input to (default: str).
    :return: The converted input.
    """
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

def calculate_estate_distribution(total_estate, num_children, spouse_share_percentage):
    """
    Calculate the estate distribution based on Louisiana estate planning laws.
    :param total_estate: Total value of the estate.
    :param num_children: Number of children.
    :param spouse_share_percentage: Percentage of estate allocated to the spouse.
    :return: A dictionary with the distribution details.
    """
    if num_children < 0 or spouse_share_percentage < 0 or spouse_share_percentage > 100:
        raise ValueError("Invalid input values for estate distribution calculation.")
    
    spouse_share = total_estate * (spouse_share_percentage / 100)
    remaining_estate = total_estate - spouse_share
    child_share = remaining_estate / num_children if num_children > 0 else 0

    return {
        "spouse_share": round(spouse_share, 2),
        "child_share": round(child_share, 2),
        "remaining_estate": round(remaining_estate, 2)
    }

def calculate_business_succession(total_business_value, successor_percentage):
    """
    Calculate the business succession allocation.
    :param total_business_value: Total value of the business.
    :param successor_percentage: Percentage of business allocated to the successor.
    :return: A dictionary with the succession details.
    """
    if successor_percentage < 0 or successor_percentage > 100:
        raise ValueError("Invalid successor percentage for business succession calculation.")
    
    successor_share = total_business_value * (successor_percentage / 100)
    remaining_business_value = total_business_value - successor_share

    return {
        "successor_share": round(successor_share, 2),
        "remaining_business_value": round(remaining_business_value, 2)
    }

def main():
    """
    Main function to run the estate planning calculator.
    """
    print("Welcome to the Louisiana Estate Planning Calculator!")
    
    try:
        # Estate Planning Inputs
        total_estate = get_user_input("Enter the total value of the estate ($): ", float)
        num_children = get_user_input("Enter the number of children: ", int)
        spouse_share_percentage = get_user_input("Enter the percentage of estate allocated to the spouse (%): ", float)

        # Business Succession Inputs
        total_business_value = get_user_input("Enter the total value of the business ($): ", float)
        successor_percentage = get_user_input("Enter the percentage of business allocated to the successor (%): ", float)

        # Calculate Estate Distribution
        estate_distribution = calculate_estate_distribution(total_estate, num_children, spouse_share_percentage)
        print("\nEstate Distribution:")
        print(f"Spouse Share: ${estate_distribution['spouse_share']}")
        print(f"Child Share (per child): ${estate_distribution['child_share']}")
        print(f"Remaining Estate: ${estate_distribution['remaining_estate']}")

        # Calculate Business Succession
        business_succession = calculate_business_succession(total_business_value, successor_percentage)
        print("\nBusiness Succession:")
        print(f"Successor Share: ${business_succession['successor_share']}")
        print(f"Remaining Business Value: ${business_succession['remaining_business_value']}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nThank you for using the Louisiana Estate Planning Calculator!")

if __name__ == "__main__":
    main()
```
