"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unitedairlines-vn.com
Prompt: Create a Python function to determine the eligibility for ticket refunds or changes based on United Airlines Vietnam's refund and exchange policies.
Generated: DETERMINISTIC_6bd870fd5d924a8b
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TicketPolicy:
    def __init__(self, ticket_type, travel_date, purchase_date, is_refundable, has_change_fee):
        """
        Initializes the TicketPolicy class with the necessary attributes.

        :param ticket_type: str - The type of ticket (e.g., 'Economy', 'Business')
        :param travel_date: str - The travel date in 'YYYY-MM-DD' format
        :param purchase_date: str - The purchase date in 'YYYY-MM-DD' format
        :param is_refundable: bool - Indicates if the ticket is refundable
        :param has_change_fee: bool - Indicates if there is a fee for changing the ticket
        """
        self.ticket_type = ticket_type
        self.travel_date = travel_date
        self.purchase_date = purchase_date
        self.is_refundable = is_refundable
        self.has_change_fee = has_change_fee

    def is_within_refund_period(self):
        """
        Checks if the ticket is within the refund period.

        :return: bool - True if within the refund period, False otherwise
        """
        from datetime import datetime, timedelta

        purchase_date = datetime.strptime(self.purchase_date, '%Y-%m-%d')
        current_date = datetime.now()

        # Define a refund period of 24 hours from the purchase time
        refund_period = timedelta(hours=24)

        return (current_date - purchase_date) < refund_period

    def check_eligibility(self):
        """
        Determines the eligibility for ticket refunds or changes.

        :return: str - Message indicating eligibility status
        """
        try:
            if self.is_refundable:
                if self.is_within_refund_period():
                    return "Eligible for full refund within 24 hours of purchase."
                else:
                    return "Eligible for refund, but outside 24-hour purchase window."
            else:
                if self.has_change_fee:
                    return "Not eligible for refund, but changes can be made with a fee."
                else:
                    return "Not eligible for refund or changes."
        except Exception as e:
            return f"Error determining eligibility: {str(e)}"

# Example usage
if __name__ == "__main__":
    ticket = TicketPolicy(ticket_type='Economy', 
                          travel_date='2023-12-01', 
                          purchase_date='2023-10-01', 
                          is_refundable=True, 
                          has_change_fee=False)
    
    eligibility_message = ticket.check_eligibility()
    print(eligibility_message)
```
