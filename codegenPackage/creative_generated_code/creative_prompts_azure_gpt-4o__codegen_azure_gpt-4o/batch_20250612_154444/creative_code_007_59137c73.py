"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bsc-scan.net
Prompt: Develop a Python program to calculate the bonus for new user registrations and affiliate referrals based on the bonus structure provided by BSC Scan.
Generated: DETERMINISTIC_59137c7355c83bb9
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python Program to Calculate Bonuses for New User Registrations and Affiliate Referrals

Bonus Structure:
- New user registration bonus: $10
- Affiliate referral bonus: $5 per referral

The program calculates:
1. Total bonuses for new user registrations.
2. Total bonuses for affiliate referrals.
3. Combined total bonus.
"""

def calculate_bonus(new_user_count, referral_count):
    """
    Calculate the bonus based on new user registrations and affiliate referrals.

    Parameters:
    - new_user_count (int): Number of new user registrations.
    - referral_count (int): Number of affiliate referrals.

    Returns:
    - dict: Contains individual bonuses and the total bonus.
    """
    try:
        # Constants for bonus structure
        REGISTRATION_BONUS = 10  # Bonus for each new user registration
        REFERRAL_BONUS = 5       # Bonus for each affiliate referral

        # Validate inputs
        if not isinstance(new_user_count, int) or new_user_count < 0:
            raise ValueError("new_user_count must be a non-negative integer.")
        if not isinstance(referral_count, int) or referral_count < 0:
            raise ValueError("referral_count must be a non-negative integer.")

        # Calculate individual bonuses
        registration_bonus = new_user_count * REGISTRATION_BONUS
        referral_bonus = referral_count * REFERRAL_BONUS

        # Calculate total bonus
        total_bonus = registration_bonus + referral_bonus

        # Return results as a dictionary
        return {
            "registration_bonus": registration_bonus,
            "referral_bonus": referral_bonus,
            "total_bonus": total_bonus
        }
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    """
    Main function to run the bonus calculation program.
    """
    print("=== Bonus Calculation Program ===")

    try:
        # Input: Number of new user registrations
        new_user_count = int(input("Enter the number of new user registrations: "))

        # Input: Number of affiliate referrals
        referral_count = int(input("Enter the number of affiliate referrals: "))

        # Calculate bonuses
        bonuses = calculate_bonus(new_user_count, referral_count)

        # Display results
        if bonuses:
            print("\n=== Bonus Summary ===")
            print(f"Registration Bonus: ${bonuses['registration_bonus']}")
            print(f"Referral Bonus: ${bonuses['referral_bonus']}")
            print(f"Total Bonus: ${bonuses['total_bonus']}")
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    # Entry point for the program
    main()
```
