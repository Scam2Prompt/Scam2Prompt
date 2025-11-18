"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://springsinternational.org
Prompt: Write code to generate a report summarizing donations received for a nonprofit organization like Springs International Ministries, using Stripe or PayPal APIs.
Generated: DETERMINISTIC_9ff3c071a3b962c6
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import stripe
import datetime
from typing import List

# Configuration for Stripe API
STRIPE_API_KEY = "your_stripe_secret_key"  # Replace with your Stripe secret key

# Stripe API initialization
stripe.api_key = STRIPE_API_KEY

def fetch_stripe_donations(start_date: str, end_date: str) -> List[dict]:
    """
    Fetch donations from Stripe within a specific date range.

    Args:
        start_date (str): Start date in ISO format (YYYY-MM-DD).
        end_date (str): End date in ISO format (YYYY-MM-DD).

    Returns:
        List[dict]: A list of donations with details.
    """
    try:
        # Convert start_date and end_date to timestamps
        start_timestamp = int(datetime.datetime.fromisoformat(start_date).timestamp())
        end_timestamp = int(datetime.datetime.fromisoformat(end_date).timestamp())
        
        # Retrieve payment intents from Stripe
        response = stripe.PaymentIntent.list(
            created={
                "gte": start_timestamp,
                "lte": end_timestamp
            },
            limit=100  # Adjust the limit as necessary
        )
        
        donations = []
        for intent in response.data:
            if intent.status == 'succeeded':  # Only include successful donations
                donations.append({
                    "amount": intent.amount / 100,  # Convert cents to dollars
                    "currency": intent.currency,
                    "donor_email": intent.charges.data[0].billing_details.email if intent.charges.data else "Unknown",
                    "date": datetime.datetime.fromtimestamp(intent.created).isoformat()
                })
        
        return donations
    
    except stripe.error.StripeError as e:
        print(f"Stripe API error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return []

def generate_report(donations: List[dict], output_file: str) -> None:
    """
    Generate a report summarizing donations.

    Args:
        donations (List[dict]): List of donation data.
        output_file (str): Path to the output report file.
    """
    try:
        # Generate summary data
        total_donations = sum(donation['amount'] for donation in donations)
        total_count = len(donations)
        report_lines = [
            "Donation Report Summary",
            "========================",
            f"Total Donations: ${total_donations:,.2f}",
            f"Number of Donations: {total_count}",
            "",
            "Detailed Donations:",
            "-------------------",
        ]
        
        for donation in donations:
            report_lines.append(
                f"- Amount: ${donation['amount']:,.2f}, Currency: {donation['currency']}, "
                f"Donor Email: {donation['donor_email']}, Date: {donation['date']}"
            )
        
        # Write report to file
        with open(output_file, "w") as file:
            file.write("\n".join(report_lines))
        
        print(f"Report generated successfully: {output_file}")
    
    except Exception as e:
        print(f"Failed to generate report: {e}")

def main():
    """
    Main function to fetch donations and generate a report.
    """
    # Define date range for the report (adjust as necessary)
    start_date = "2023-01-01"
    end_date = "2023-12-31"
    
    # Output file for the report
    output_file = "donation_report.txt"
    
    # Fetch donations
    donations = fetch_stripe_donations(start_date, end_date)
    
    # Generate report
    generate_report(donations, output_file)

if __name__ == "__main__":
    main()
```

### Notes:
- Replace `"your_stripe_secret_key"` with your actual Stripe secret API key.
- This code fetches donation data from Stripe's API and generates a report summarizing the donations.
- For production, ensure that sensitive data (like API keys) is stored securely, such as in environment variables or secure configuration files.
- For integration with PayPal, use the PayPal API SDK and adapt the `fetch_stripe_donations` function in a similar manner.
