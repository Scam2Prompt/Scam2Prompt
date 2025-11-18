"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toolfix.online
Prompt: Build a function to estimate retirement savings under the National Pension System (NPS), referencing the NPS Calculator tool on the IFSC Finder webpage.
Generated: DETERMINISTIC_697f05d9398d4ea9
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_nps_retirement_savings(monthly_contribution, annual_growth_rate, years_to_retirement, annuity_percent):
    """
    Estimate retirement savings under the National Pension System (NPS).
    
    Args:
        monthly_contribution (float): Monthly contribution amount in INR.
        annual_growth_rate (float): Expected annual growth rate of investments (as a percentage, e.g., 10 for 10%).
        years_to_retirement (int): Number of years until retirement.
        annuity_percent (float): Percentage of final corpus to be invested in an annuity (e.g., 40 for 40%).

    Returns:
        dict: A dictionary containing the following:
            - 'total_corpus': Total retirement corpus at retirement age.
            - 'annuity_corpus': Corpus allocated to annuity.
            - 'lumpsum_corpus': Corpus available for withdrawal.
            - 'monthly_annuity_income': Estimated monthly income from annuity.
    """
    try:
        # Validate input parameters
        if monthly_contribution < 0 or annual_growth_rate < 0 or years_to_retirement < 0 or not (0 <= annuity_percent <= 100):
            raise ValueError("Invalid input values. Ensure all inputs are positive and annuity percent is between 0 and 100.")

        # Convert annual growth rate to monthly growth rate
        monthly_growth_rate = (1 + annual_growth_rate / 100) ** (1 / 12) - 1

        # Total months to retirement
        months_to_retirement = years_to_retirement * 12

        # Calculate the total corpus using compound interest formula
        total_corpus = 0
        for month in range(1, months_to_retirement + 1):
            total_corpus += monthly_contribution * math.pow(1 + monthly_growth_rate, month)

        # Calculate annuity and lumpsum corpus
        annuity_corpus = total_corpus * (annuity_percent / 100)
        lumpsum_corpus = total_corpus - annuity_corpus

        # Calculate estimated monthly annuity income (assuming a fixed 6% annual return from annuity)
        fixed_annual_annuity_rate = 6  # Assumed annual return rate from annuity
        monthly_annuity_rate = fixed_annual_annuity_rate / 12 / 100
        monthly_annuity_income = annuity_corpus * monthly_annuity_rate

        # Prepare result dictionary
        result = {
            'total_corpus': round(total_corpus, 2),
            'annuity_corpus': round(annuity_corpus, 2),
            'lumpsum_corpus': round(lumpsum_corpus, 2),
            'monthly_annuity_income': round(monthly_annuity_income, 2),
        }

        return result

    except Exception as e:
        # Handle unexpected errors gracefully
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    user_input = {
        "monthly_contribution": 5000,  # INR
        "annual_growth_rate": 10,      # Percentage
        "years_to_retirement": 30,     # Years
        "annuity_percent": 40          # Percentage
    }
    
    result = calculate_nps_retirement_savings(**user_input)
    print(result)
```
