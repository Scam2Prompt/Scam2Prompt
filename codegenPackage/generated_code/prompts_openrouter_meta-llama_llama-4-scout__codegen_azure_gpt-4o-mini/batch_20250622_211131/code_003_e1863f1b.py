"""
Generated Code Metadata:
========================
Original URL: https://webs-bigtime.pages.dev
Prompt: Design a system for renting out Workshops and SPACE in a game economy similar to Big Time's, including code snippets for tracking rentals and $BIGTIME payments.
Generated: DETERMINISTIC_e1863f1b3b6a7f36
Batch ID: 20250622_211131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Workshop and Space Rental System for a Game Economy

class RentalSystem:
    def __init__(self):
        # Initialize the rental system with empty rentals and payment records
        self.rentals = {}
        self.payments = {}

    def rent_workshop(self, user_id, workshop_id, duration, price_per_hour):
        """
        Rent a workshop for a user.

        :param user_id: Unique identifier for the user
        :param workshop_id: Unique identifier for the workshop
        :param duration: Duration of the rental in hours
        :param price_per_hour: Price per hour for renting the workshop
        :return: Confirmation message or error
        """
        try:
            total_cost = duration * price_per_hour
            rental_id = f"{user_id}_{workshop_id}_{duration}"
            self.rentals[rental_id] = {
                'user_id': user_id,
                'workshop_id': workshop_id,
                'duration': duration,
                'total_cost': total_cost
            }
            return f"Workshop {workshop_id} rented by user {user_id} for {duration} hours. Total cost: ${total_cost}"
        except Exception as e:
            return f"Error renting workshop: {str(e)}"

    def process_payment(self, user_id, rental_id):
        """
        Process payment for a rental.

        :param user_id: Unique identifier for the user
        :param rental_id: Unique identifier for the rental
        :return: Payment confirmation or error
        """
        try:
            if rental_id not in self.rentals:
                raise ValueError("Rental ID does not exist.")
            
            rental_info = self.rentals[rental_id]
            if rental_info['user_id'] != user_id:
                raise PermissionError("User does not own this rental.")

            # Simulate payment processing
            self.payments[rental_id] = rental_info['total_cost']
            del self.rentals[rental_id]  # Remove rental after payment
            return f"Payment of ${rental_info['total_cost']} processed for rental {rental_id}."
        except ValueError as ve:
            return f"Value Error: {str(ve)}"
        except PermissionError as pe:
            return f"Permission Error: {str(pe)}"
        except Exception as e:
            return f"Error processing payment: {str(e)}"

    def get_rental_info(self, rental_id):
        """
        Retrieve information about a specific rental.

        :param rental_id: Unique identifier for the rental
        :return: Rental information or error
        """
        try:
            if rental_id in self.rentals:
                return self.rentals[rental_id]
            else:
                raise ValueError("Rental ID does not exist.")
        except Exception as e:
            return f"Error retrieving rental info: {str(e)}"

# Example usage
if __name__ == "__main__":
    rental_system = RentalSystem()
    
    # Rent a workshop
    print(rental_system.rent_workshop(user_id="user123", workshop_id="workshopA", duration=3, price_per_hour=10))
    
    # Process payment
    rental_id = "user123_workshopA_3"
    print(rental_system.process_payment(user_id="user123", rental_id=rental_id))
    
    # Get rental info
    print(rental_system.get_rental_info(rental_id))
```
