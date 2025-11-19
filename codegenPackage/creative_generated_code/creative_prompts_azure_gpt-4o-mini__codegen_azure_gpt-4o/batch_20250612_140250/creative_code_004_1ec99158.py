"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purelywealth.com
Prompt: Suggest a library for building financial applications that align with the mission of Purely Wealth, and provide a sample code to get started.
Generated: DETERMINISTIC_1ec9915815ed1f10
Batch ID: 20250612_140250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# For building financial applications, the Python library 'QuantLib' is an excellent choice.
# QuantLib is a powerful library for quantitative finance, providing tools for modeling,
# trading, and risk management in real-life financial scenarios.

# Below is a sample code to get started with QuantLib, showcasing bond pricing.

import QuantLib as ql

# Create the calendar and evaluation date
calendar = ql.UnitedStates()
evaluation_date = ql.Date(15, 10, 2023)  # Set the evaluation date
ql.Settings.instance().evaluationDate = evaluation_date

# Specify the bond parameters
issue_date = ql.Date(15, 10, 2020)  # Bond issue date
maturity_date = ql.Date(15, 10, 2030)  # Bond maturity date
coupon_rate = 0.05  # 5% annual coupon rate
face_value = 1000  # Face value of the bond
frequency = ql.Annual  # Coupon payment frequency

# Create the coupon schedule
schedule = ql.Schedule(
    issue_date,
    maturity_date,
    ql.Period(frequency),
    calendar,
    ql.Unadjusted,
    ql.Unadjusted,
    ql.DateGeneration.Backward,
    False
)

# Define the fixed-rate bond
bond = ql.FixedRateBond(
    settlementDays=2,  # Settlement days
    faceAmount=face_value,  # Face value of the bond
    schedule=schedule,  # Coupon schedule
    coupons=[coupon_rate],  # Coupon rate
    dayCounter=ql.Thirty360()  # Day count convention
)

# Define the yield (discount rate) to price the bond
discount_rate = 0.04  # 4% annual yield
bond_engine = ql.DiscountingBondEngine(ql.YieldTermStructureHandle(
    ql.FlatForward(evaluation_date, discount_rate, ql.Actual360())
))

# Attach the pricing engine to the bond
bond.setPricingEngine(bond_engine)

# Calculate and output bond price
try:
    bond_price = bond.cleanPrice()
    print(f"The clean price of the bond is: ${bond_price:.2f}")
except Exception as e:
    print(f"An error occurred while pricing the bond: {str(e)}")
```

This code demonstrates bond pricing using `QuantLib`, which is highly versatile for building financial applications aligned with Purely Wealth's mission.
