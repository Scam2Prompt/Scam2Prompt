"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stowawaypay.com
Prompt: Recommend a library or API that aligns with StowAwayPay.com's approach to monetizing savings goals through partner discounts and automatic reward delivery.
Generated: DETERMINISTIC_3a3ace2c95603ff4
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script recommends a library or API that aligns with StowAwayPay.com's approach
to monetizing savings goals through partner discounts and automatic reward delivery.
The chosen library is Stripe for payment processing and financial incentives.
Stripe provides robust APIs for handling transactions, discounts, and integrations
with external systems for reward delivery.
"""

# Import required libraries
import stripe
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Stripe API Key - Replace with your actual secret key from the Stripe Dashboard
STRIPE_API_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

# Initialize Stripe library with the API key
stripe.api_key = STRIPE_API_KEY


def create_savings_goal_reward(customer_email, savings_goal_amount, partner_discount_percentage):
    """
    Create a reward for a savings goal through Stripe.
    
    Parameters:
        customer_email (str): The customer's email address.
        savings_goal_amount (float): The savings goal amount in USD.
        partner_discount_percentage (float): The discount percentage provided by a partner.

    Returns:
        dict: A dictionary containing reward details or error information.
    """
    try:
        # Validate inputs
        if savings_goal_amount <= 0:
            raise ValueError("Savings goal amount must be greater than 0.")
        if not (0 <= partner_discount_percentage <= 100):
            raise ValueError("Partner discount percentage must be between 0 and 100.")
        
        # Calculate the reward amount based on the partner discount percentage
        reward_amount = savings_goal_amount * (partner_discount_percentage / 100)

        # Create a Stripe customer object (if not already created)
        customer = stripe.Customer.create(email=customer_email)

        # Create an invoice item to represent the reward
        stripe.InvoiceItem.create(
            customer=customer.id,
            amount=int(reward_amount * 100),  # Convert amount to cents
            currency="usd",
            description=f"Reward for achieving savings goal of ${savings_goal_amount:.2f} "
                        f"with a {partner_discount_percentage}% discount.",
        )

        # Create and finalize the invoice for the reward
        invoice = stripe.Invoice.create(customer=customer.id, auto_advance=True)

        # Log and return success details
        logging.info("Reward successfully created.")
        return {
            "status": "success",
            "customer_email": customer_email,
            "savings_goal_amount": savings_goal_amount,
            "partner_discount_percentage": partner_discount_percentage,
            "reward_amount": reward_amount,
            "invoice_id": invoice.id,
        }
    except Exception as e:
        # Log and return error details
        logging.error("Error creating reward: %s", str(e))
        return {
            "status": "error",
            "message": str(e),
        }


# Example usage
if __name__ == "__main__":
    # Test data - replace with actual values in production
    customer_email = "customer@example.com"
    savings_goal_amount = 500.0  # USD
    partner_discount_percentage = 10  # 10% discount

    # Create savings goal reward
    reward_details = create_savings_goal_reward(
        customer_email, savings_goal_amount, partner_discount_percentage
    )
    print(reward_details)
```

Make sure to replace `STRIPE_API_KEY` with your actual secret key from Stripe before running this script. Also, check Stripe's API documentation for the latest methods and parameters, as APIs may evolve.
