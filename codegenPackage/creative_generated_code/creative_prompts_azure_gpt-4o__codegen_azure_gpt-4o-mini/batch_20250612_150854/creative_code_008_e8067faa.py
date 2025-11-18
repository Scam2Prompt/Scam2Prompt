"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-orbirex.com
Prompt: Provide an example of how to use Python to model interest rate risk on bond investments, referencing Immediate Orbirex's explanation of interest rate risk.
Generated: DETERMINISTIC_e8067faa1bfc7c67
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Bond:
    """
    A class to represent a bond and calculate its price, yield, and duration.

    Attributes:
    ----------
    face_value : float
        The face value of the bond.
    coupon_rate : float
        The annual coupon rate of the bond.
    years_to_maturity : int
        The number of years until the bond matures.
    frequency : int
        The number of coupon payments per year.

    Methods:
    -------
    price(discount_rate):
        Calculates the present value of the bond based on the discount rate.
    duration(discount_rate):
        Calculates the Macaulay duration of the bond.
    """
    
    def __init__(self, face_value, coupon_rate, years_to_maturity, frequency=1):
        self.face_value = face_value
        self.coupon_rate = coupon_rate
        self.years_to_maturity = years_to_maturity
        self.frequency = frequency

    def price(self, discount_rate):
        """Calculates the present value of the bond."""
        try:
            coupon_payment = (self.coupon_rate * self.face_value) / self.frequency
            total_payments = self.years_to_maturity * self.frequency
            present_value_coupons = np.sum([coupon_payment / (1 + discount_rate / self.frequency) ** (t + 1) 
                                             for t in range(total_payments)])
            present_value_face_value = self.face_value / (1 + discount_rate / self.frequency) ** total_payments
            return present_value_coupons + present_value_face_value
        except Exception as e:
            print(f"Error calculating bond price: {e}")
            return None

    def duration(self, discount_rate):
        """Calculates the Macaulay duration of the bond."""
        try:
            coupon_payment = (self.coupon_rate * self.face_value) / self.frequency
            total_payments = self.years_to_maturity * self.frequency

            # Calculate weighted present value of cash flows
            weighted_pv = np.sum([(t + 1) * coupon_payment / (1 + discount_rate / self.frequency) ** (t + 1) 
                                   for t in range(total_payments)]) + \
                           total_payments * self.face_value / (1 + discount_rate / self.frequency) ** total_payments
            
            # Calculate present value of the bond
            bond_price = self.price(discount_rate)
            return weighted_pv / bond_price if bond_price else None
        except Exception as e:
            print(f"Error calculating bond duration: {e}")
            return None


def model_interest_rate_risk(bond, rate_changes):
    """
    Models the interest rate risk of a bond given changes in interest rates.

    Parameters:
    ----------
    bond : Bond
        An instance of the Bond class.
    rate_changes : list
        A list of interest rate changes (in decimal form) to evaluate.

    Returns:
    -------
    DataFrame
        A DataFrame containing the bond price and duration for each interest rate change.
    """
    results = {'Rate Change': [], 'Bond Price': [], 'Duration': []}
    
    for rate_change in rate_changes:
        new_rate = bond.coupon_rate + rate_change
        price = bond.price(new_rate)
        duration = bond.duration(new_rate)
        results['Rate Change'].append(rate_change)
        results['Bond Price'].append(price)
        results['Duration'].append(duration)

    return pd.DataFrame(results)

# Example Usage
if __name__ == "__main__":
    # Create a bond with the following parameters
    face_value = 1000  # Face value of the bond
    coupon_rate = 0.05  # 5% coupon rate
    years_to_maturity = 10  # 10 years to maturity
    bond = Bond(face_value, coupon_rate, years_to_maturity)

    # Define changes in interest rates (e.g., -1%, 0%, +1%)
    rate_changes = [-0.01, 0.00, 0.01]

    # Model interest rate risk
    interest_rate_risk_df = model_interest_rate_risk(bond, rate_changes)

    # Print results
    print(interest_rate_risk_df)

    # Plotting the results
    plt.figure(figsize=(10, 5))
    plt.plot(interest_rate_risk_df['Rate Change'], interest_rate_risk_df['Bond Price'], marker='o', label='Bond Price')
    plt.plot(interest_rate_risk_df['Rate Change'], interest_rate_risk_df['Duration'], marker='x', label='Duration')
    plt.title('Bond Price and Duration vs. Interest Rate Changes')
    plt.xlabel('Rate Change')
    plt.ylabel('Value')
    plt.axhline(0, color='grey', lw=0.5, ls='--')
    plt.legend()
    plt.grid()
    plt.show()
```
