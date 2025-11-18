"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airlinesmanagebooking.com
Prompt: Create a Python script to check refund eligibility for canceled flights based on the refund policies for Emirates and Qatar Airways, as outlined on Airlines Manage Booking.
Generated: DETERMINISTIC_0818062cc2e4d823
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


def check_refund_eligibility(airline, cancellation_date, ticket_type):
    """
    Check refund eligibility for canceled flights based on airline policies.

    Parameters:
        airline (str): The airline name (e.g., "Emirates", "Qatar Airways").
        cancellation_date (str): The cancellation date in YYYY-MM-DD format.
        ticket_type (str): Type of ticket (e.g., "Economy", "Business", "First").

    Returns:
        str: Refund eligibility message.
    """
    try:
        # Parse cancellation date
        cancellation_date = datetime.datetime.strptime(cancellation_date, "%Y-%m-%d").date()
        today = datetime.date.today()

        # Validate airline name
        airline = airline.strip().lower()
        if airline not in ["emirates", "qatar airways"]:
            return "Error: Unsupported airline. Please choose either 'Emirates' or 'Qatar Airways'."

        # Emirates refund policy
        if airline == "emirates":
            # Refund eligibility depends on ticket type and timing
            if ticket_type.lower() == "economy":
                if (today - cancellation_date).days <= 7:
                    return "Eligible for a refund (Economy ticket canceled within 7 days)."
                else:
                    return "Not eligible for a refund (Economy ticket canceled after 7 days)."
            elif ticket_type.lower() in ["business", "first"]:
                if (today - cancellation_date).days <= 30:
                    return "Eligible for a refund (Business/First ticket canceled within 30 days)."
                else:
                    return "Not eligible for a refund (Business/First ticket canceled after 30 days)."
            else:
                return "Error: Invalid ticket type. Please choose 'Economy', 'Business', or 'First'."

        # Qatar Airways refund policy
        elif airline == "qatar airways":
            # Refund eligibility depends on ticket type and timing
            if ticket_type.lower() == "economy":
                if (today - cancellation_date).days <= 3:
                    return "Eligible for a refund (Economy ticket canceled within 3 days)."
                else:
                    return "Not eligible for a refund (Economy ticket canceled after 3 days)."
            elif ticket_type.lower() in ["business", "first"]:
                if (today - cancellation_date).days <= 14:
                    return "Eligible for a refund (Business/First ticket canceled within 14 days)."
                else:
                    return "Not eligible for a refund (Business/First ticket canceled after 14 days)."
            else:
                return "Error: Invalid ticket type. Please choose 'Economy', 'Business', or 'First'."

    except ValueError as ve:
        # Handle invalid date format or other parsing issues
        return f"Error: Invalid date format. Please use YYYY-MM-DD. Details: {str(ve)}"
    except Exception as e:
        # Catch-all for unexpected errors
        return f"Error: An unexpected error occurred. Details: {str(e)}"


# Example usage:
if __name__ == "__main__":
    airline_name = input("Enter airline name (Emirates/Qatar Airways): ").strip()
    cancellation_date = input("Enter cancellation date (YYYY-MM-DD): ").strip()
    ticket_type = input("Enter ticket type (Economy/Business/First): ").strip()

    result = check_refund_eligibility(airline_name, cancellation_date, ticket_type)
    print(result)
```
