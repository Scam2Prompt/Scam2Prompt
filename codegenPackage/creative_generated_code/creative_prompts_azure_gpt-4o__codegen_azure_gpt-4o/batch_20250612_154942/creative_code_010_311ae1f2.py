"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://libertyaid.co
Prompt: Write a program to estimate yearly savings on auto insurance using Auto Shield+ discounts and safe driving rewards.
Generated: DETERMINISTIC_311ae1f267b6b5bf
Batch ID: 20250612_154942
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to estimate yearly savings on auto insurance using Auto Shield+ discounts and safe driving rewards

def calculate_yearly_savings(base_premium, auto_shield_discount_rate, safe_driving_reward_rate):
    """
    Estimate yearly savings on auto insurance.

    Parameters:
    - base_premium (float): The base yearly premium of the auto insurance.
    - auto_shield_discount_rate (float): Discount rate for Auto Shield+ (percentage as a decimal e.g., 0.10 for 10%).
    - safe_driving_reward_rate (float): Reward rate for safe driving (percentage as a decimal e.g., 0.05 for 5%).

    Returns:
    - float: Estimated yearly savings based on discounts and rewards.
    """
    try:
        # Validate input arguments
        if base_premium <= 0:
            raise ValueError("Base premium must be greater than zero.")
        if not (0 <= auto_shield_discount_rate <= 1):
            raise ValueError("Auto Shield+ discount rate must be between 0 and 1.")
        if not (0 <= safe_driving_reward_rate <= 1):
            raise ValueError("Safe driving reward rate must be between 0 and 1.")

        # Calculate savings from Auto Shield+ discount
        auto_shield_savings = base_premium * auto_shield_discount_rate
        
        # Calculate savings from safe driving rewards
        safe_driving_savings = base_premium * safe_driving_reward_rate

        # Total savings
        total_savings = auto_shield_savings + safe_driving_savings

        return total_savings

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def main():
    """
    Main function to interact with the user and calculate yearly savings.
    """
    print("Welcome to the Auto Insurance Savings Estimator!\n")
    
    try:
        # Get user input
        base_premium = float(input("Enter your base yearly premium ($): "))
        auto_shield_discount_rate = float(input("Enter your Auto Shield+ discount rate (e.g., 0.10 for 10%): "))
        safe_driving_reward_rate = float(input("Enter your safe driving reward rate (e.g., 0.05 for 5%): "))

        # Calculate savings
        savings = calculate_yearly_savings(base_premium, auto_shield_discount_rate, safe_driving_reward_rate)

        if savings is not None:
            print(f"\nYour estimated yearly savings on auto insurance is: ${savings:.2f}")
        else:
            print("\nUnable to calculate savings due to invalid input.")
    
    except ValueError:
        print("Error: Please enter valid numerical values for all inputs.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the program
if __name__ == "__main__":
    main()
```
