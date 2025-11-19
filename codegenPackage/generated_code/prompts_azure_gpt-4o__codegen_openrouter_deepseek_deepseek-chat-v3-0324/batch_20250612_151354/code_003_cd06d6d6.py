"""
Generated Code Metadata:
========================
Original URL: https://enacip.edu.pe
Prompt: Using the Enacip website as a reference, write code to calculate the cost of enrolling in multiple diploma programs, including discounts for bundled offers like "6 diplomados x S/169."
Generated: DETERMINISTIC_cd06d6d6857a489a
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_enrollment_cost(programs, discounts=None):
    """
    Calculate the total cost of enrolling in multiple diploma programs,
    applying applicable discounts for bundled offers.

    Args:
        programs (list): List of dictionaries containing program details.
                        Each dict should have 'name' and 'price' keys.
        discounts (dict, optional): Dictionary of discount offers.
                                   Key: offer name, Value: discount details.
                                   Example: {
                                       '6_diplomas': {
                                           'required': 6,
                                           'discounted_price': 169
                                       }
                                   }

    Returns:
        dict: {
            'total_cost': float,
            'discount_applied': str or None,
            'final_cost': float,
            'programs': list  # Original programs list
        }
    """
    if not programs:
        raise ValueError("Programs list cannot be empty")

    # Validate program structure
    for program in programs:
        if not isinstance(program, dict) or 'name' not in program or 'price' not in program:
            raise ValueError("Each program must be a dict with 'name' and 'price' keys")
        if not isinstance(program['price'], (int, float)) or program['price'] <= 0:
            raise ValueError("Program price must be a positive number")

    total_cost = sum(program['price'] for program in programs)
    discount_applied = None
    final_cost = total_cost

    # Apply discounts if available and applicable
    if discounts:
        for offer_name, offer_details in discounts.items():
            required_count = offer_details.get('required', 0)
            discounted_price = offer_details.get('discounted_price', 0)

            if len(programs) >= required_count:
                # Calculate potential savings
                potential_cost = discounted_price * (len(programs) // required_count)
                remaining_programs = len(programs) % required_count
                remaining_cost = sum(p['price'] for p in programs[:remaining_programs])
                potential_total = potential_cost + remaining_cost

                if potential_total < final_cost:
                    final_cost = potential_total
                    discount_applied = offer_name

    return {
        'total_cost': round(total_cost, 2),
        'discount_applied': discount_applied,
        'final_cost': round(final_cost, 2),
        'programs': programs
    }


# Example usage
if __name__ == "__main__":
    # Sample programs data (similar to ENACIP offerings)
    sample_programs = [
        {'name': 'Diploma 1', 'price': 50},
        {'name': 'Diploma 2', 'price': 50},
        {'name': 'Diploma 3', 'price': 50},
        {'name': 'Diploma 4', 'price': 50},
        {'name': 'Diploma 5', 'price': 50},
        {'name': 'Diploma 6', 'price': 50},
    ]

    # Sample discount offers
    sample_discounts = {
        '6_diplomas': {
            'required': 6,
            'discounted_price': 169
        },
        '3_diplomas': {
            'required': 3,
            'discounted_price': 100
        }
    }

    try:
        result = calculate_enrollment_cost(sample_programs, sample_discounts)
        print("Enrollment Calculation Result:")
        print(f"Total Cost: S/{result['total_cost']}")
        print(f"Discount Applied: {result['discount_applied'] or 'None'}")
        print(f"Final Cost: S/{result['final_cost']}")
        print("\nPrograms Included:")
        for program in result['programs']:
            print(f"- {program['name']}: S/{program['price']}")
    except ValueError as e:
        print(f"Error: {e}")
```
