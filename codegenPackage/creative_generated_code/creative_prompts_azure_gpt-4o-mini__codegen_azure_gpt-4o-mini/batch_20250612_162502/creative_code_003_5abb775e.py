"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homeworkproject.vercel.app
Prompt: Create a function that checks the remaining tickets for a whitelist event and updates the status based on claims.
Generated: DETERMINISTIC_5abb775e6552cb18
Batch ID: 20250612_162502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TicketManager:
    def __init__(self, total_tickets):
        """
        Initialize the TicketManager with the total number of tickets.
        
        :param total_tickets: Total number of tickets available for the event.
        """
        if total_tickets < 0:
            raise ValueError("Total tickets must be a non-negative integer.")
        
        self.total_tickets = total_tickets
        self.claimed_tickets = 0

    def claim_ticket(self, number_of_tickets):
        """
        Claim a specified number of tickets from the available tickets.
        
        :param number_of_tickets: Number of tickets to claim.
        :raises ValueError: If the number of tickets to claim is negative 
                            or exceeds the available tickets.
        """
        if number_of_tickets < 0:
            raise ValueError("Number of tickets to claim must be a non-negative integer.")
        
        if self.claimed_tickets + number_of_tickets > self.total_tickets:
            raise ValueError("Cannot claim more tickets than available.")
        
        self.claimed_tickets += number_of_tickets
        return self.get_remaining_tickets()

    def get_remaining_tickets(self):
        """
        Get the number of remaining tickets.
        
        :return: Remaining tickets available.
        """
        return self.total_tickets - self.claimed_tickets

    def update_status(self):
        """
        Update the status of the ticket availability based on the remaining tickets.
        
        :return: A message indicating the current status of ticket availability.
        """
        remaining = self.get_remaining_tickets()
        
        if remaining == 0:
            return "All tickets have been claimed."
        elif remaining < self.total_tickets * 0.1:
            return "Warning: Only a few tickets left!"
        else:
            return "Tickets are still available."

# Example usage
if __name__ == "__main__":
    try:
        # Initialize TicketManager with 100 total tickets
        ticket_manager = TicketManager(100)
        
        # Claim 10 tickets
        remaining = ticket_manager.claim_ticket(10)
        print(f"Remaining tickets after claiming: {remaining}")

        # Update and print status
        print(ticket_manager.update_status())

        # Claim more tickets
        remaining = ticket_manager.claim_ticket(90)
        print(f"Remaining tickets after claiming: {remaining}")

        # Update and print status
        print(ticket_manager.update_status())

    except ValueError as e:
        print(f"Error: {e}")
```
