"""
Generated Code Metadata:
========================
Original URL: https://token-graph.net
Prompt: What are the eligibility criteria for getting up to $1,000 off on iPhone 16 Pro Max or Samsung Galaxy S25 Ultra with AT&T?
Generated: DETERMINISTIC_33f8198642445ac2
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Eligibility Criteria Checker for AT&T Discounts

class EligibilityCriteria:
    def __init__(self, phone_model, current_carrier, current_plan, trade_in_value):
        """
        Initialize eligibility criteria.

        Args:
            phone_model (str): The model of the phone (iPhone16 Pro Max or Samsung Galaxy S25 Ultra).
            current_carrier (str): The current carrier of the user.
            current_plan (str): The current plan of the user.
            trade_in_value (float): The trade-in value of the user's current phone.
        """
        self.phone_model = phone_model
        self.current_carrier = current_carrier
        self.current_plan = current_plan
        self.trade_in_value = trade_in_value

    def check_eligibility(self):
        """
        Check if the user is eligible for up to $1,000 off on the specified phone model with AT&T.

        Returns:
            dict: A dictionary containing the eligibility status and the discount amount.
        """
        try:
            # Define the eligible phone models
            eligible_phone_models = ["iPhone16 Pro Max", "Samsung Galaxy S25 Ultra"]

            # Check if the phone model is eligible
            if self.phone_model not in eligible_phone_models:
                return {"eligible": False, "discount": 0, "message": "Phone model not eligible for discount"}

            # Check if the current carrier is not AT&T
            if self.current_carrier.lower() == "at&t":
                return {"eligible": False, "discount": 0, "message": "You are already with AT&T"}

            # Define the minimum trade-in value required for the discount
            min_trade_in_value = 500

            # Check if the trade-in value meets the minimum requirement
            if self.trade_in_value < min_trade_in_value:
                return {"eligible": False, "discount": 0, "message": f"Trade-in value must be at least ${min_trade_in_value}"}

            # Define the maximum discount amount
            max_discount = 1000

            # Calculate the discount amount based on the trade-in value
            discount = min(self.trade_in_value, max_discount)

            # Check if the current plan is eligible for the discount
            eligible_plans = ["AT&T Unlimited More", "AT&T Unlimited Premium"]
            if self.current_plan not in eligible_plans:
                return {"eligible": False, "discount": 0, "message": f"Plan not eligible for discount. Eligible plans: {', '.join(eligible_plans)}"}

            return {"eligible": True, "discount": discount, "message": f"You are eligible for a discount of up to ${discount}"}

        except Exception as e:
            return {"eligible": False, "discount": 0, "message": str(e)}


def main():
    phone_model = input("Enter the phone model (iPhone16 Pro Max or Samsung Galaxy S25 Ultra): ")
    current_carrier = input("Enter your current carrier: ")
    current_plan = input("Enter your current plan: ")
    trade_in_value = float(input("Enter your trade-in value: "))

    eligibility_criteria = EligibilityCriteria(phone_model, current_carrier, current_plan, trade_in_value)
    result = eligibility_criteria.check_eligibility()

    print("Eligibility Status:")
    print(f"Eligible: {result['eligible']}")
    print(f"Discount: ${result['discount']}")
    print(f"Message: {result['message']}")


if __name__ == "__main__":
    main()
```
