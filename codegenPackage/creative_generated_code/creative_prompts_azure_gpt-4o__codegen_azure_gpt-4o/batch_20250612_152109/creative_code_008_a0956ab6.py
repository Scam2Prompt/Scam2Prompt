"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getarcadeapp.pages.dev
Prompt: Develop a tool to calculate the profitability of lending NFTs on the Arcade marketplace, factoring in APR and loan terms.
Generated: DETERMINISTIC_a0956ab61b3a934a
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def calculate_nft_profitability(nft_value, annual_percentage_rate, loan_term_days):
    """
    Calculates the profitability of lending an NFT on the Arcade marketplace.
    
    Parameters:
    nft_value (float): The value of the NFT being loaned (in USD).
    annual_percentage_rate (float): The Annual Percentage Rate (APR) offered for the loan (percentage).
    loan_term_days (int): The loan term duration in days.
    
    Returns:
    dict: A dictionary containing the total interest earned, gross profitability, and net profitability.
    """
    try:
        # Validate input types
        if not isinstance(nft_value, (int, float)) or nft_value <= 0:
            raise ValueError("NFT value must be a positive number.")
        if not isinstance(annual_percentage_rate, (int, float)) or annual_percentage_rate <= 0:
            raise ValueError("APR must be a positive number.")
        if not isinstance(loan_term_days, int) or loan_term_days <= 0:
            raise ValueError("Loan term days must be a positive integer.")

        # Calculate daily interest rate from APR
        daily_interest_rate = annual_percentage_rate / 100 / 365

        # Calculate total interest earned during the loan term
        total_interest_earned = nft_value * daily_interest_rate * loan_term_days

        # Gross profitability is the interest earned
        gross_profitability = total_interest_earned

        # Assuming no additional fees, net profitability equals gross profitability
        net_profitability = gross_profitability

        return {
            "total_interest_earned": round(total_interest_earned, 2),
            "gross_profitability": round(gross_profitability, 2),
            "net_profitability": round(net_profitability, 2)
        }

    except ValueError as ve:
        # Handle invalid input errors
        return {"error": str(ve)}

    except Exception as e:
        # Handle unexpected errors gracefully
        return {"error": f"An unexpected error occurred: {str(e)}"}


# Example usage
if __name__ == "__main__":
    try:
        print("NFT Lending Profitability Calculator")

        # Prompt user for inputs
        nft_value = float(input("Enter the NFT value (USD): "))
        apr = float(input("Enter the Annual Percentage Rate (APR in %): "))
        loan_term_days = int(input("Enter the loan term duration (in days): "))

        # Calculate profitability
        result = calculate_nft_profitability(nft_value, apr, loan_term_days)

        # Display results
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print("\nProfitability Results:")
            print(f"Total Interest Earned: ${result['total_interest_earned']}")
            print(f"Gross Profitability: ${result['gross_profitability']}")
            print(f"Net Profitability: ${result['net_profitability']}")

    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
