"""
Generated Code Metadata:
========================
Original URL: https://orlandoplasmacenters.com
Prompt: Generate a Python script to calculate the total earnings for a donor based on the compensation structure of $100-$200 per donation at Orlando Plasma Centers.
Generated: DETERMINISTIC_9ef0562148b3b61c
Batch ID: 20250622_211932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Orlando Plasma Center Donor Earnings Calculator

Calculates the total earnings for a donor based on the compensation structure
of $100-$200 per donation.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_donor_earnings(num_donations: int, compensation_per_donation: float) -> float:
    """
    Calculates the total earnings for a donor.

    Args:
    - num_donations (int): The number of donations made by the donor.
    - compensation_per_donation (float): The compensation per donation.

    Returns:
    - float: The total earnings for the donor.

    Raises:
    - ValueError: If the number of donations or compensation per donation is invalid.
    """
    if num_donations < 0:
        raise ValueError("Number of donations cannot be negative.")
    if compensation_per_donation not in [100.0, 200.0]:
        raise ValueError("Invalid compensation per donation. Must be $100 or $200.")

    total_earnings = num_donations * compensation_per_donation
    return total_earnings


def main():
    try:
        num_donations = int(input("Enter the number of donations: "))
        print("Select the compensation per donation:")
        print("1. $100")
        print("2. $200")
        choice = int(input("Enter your choice (1/2): "))

        if choice == 1:
            compensation_per_donation = 100.0
        elif choice == 2:
            compensation_per_donation = 200.0
        else:
            print("Invalid choice. Exiting.")
            return

        total_earnings = calculate_donor_earnings(num_donations, compensation_per_donation)
        print(f"Total earnings: ${total_earnings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
