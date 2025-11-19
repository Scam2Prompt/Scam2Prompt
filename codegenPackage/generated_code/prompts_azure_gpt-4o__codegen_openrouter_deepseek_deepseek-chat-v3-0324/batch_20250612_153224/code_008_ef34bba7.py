"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: Generate a script to calculate the rental cost of Yanmar mini excavators based on daily rates and rental duration, including a feature for automatic reservation confirmation.
Generated: DETERMINISTIC_ef34bba787a5fe10
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Optional, Dict

class YanmarMiniExcavatorRental:
    """
    A class to calculate rental costs for Yanmar mini excavators and handle reservations.
    """
    
    def __init__(self):
        self.excavator_rates = {
            'SV08': {'daily_rate': 150, 'weekly_rate': 800, 'monthly_rate': 2500},
            'SV17': {'daily_rate': 200, 'weekly_rate': 1100, 'monthly_rate': 3500},
            'SV40': {'daily_rate': 300, 'weekly_rate': 1600, 'monthly_rate': 5000}
        }
        self.reservations = {}
    
    def calculate_rental_cost(self, model: str, duration_days: int) -> Optional[float]:
        """
        Calculate the total rental cost based on the excavator model and rental duration.
        
        Args:
            model: The excavator model (SV08, SV17, SV40)
            duration_days: Number of rental days
            
        Returns:
            Total rental cost or None if model is invalid
        """
        if model not in self.excavator_rates:
            return None
            
        rates = self.excavator_rates[model]
        
        if duration_days >= 30:
            months = duration_days // 30
            remaining_days = duration_days % 30
            monthly_cost = months * rates['monthly_rate']
            
            if remaining_days >= 7:
                weeks = remaining_days // 7
                days = remaining_days % 7
                return monthly_cost + (weeks * rates['weekly_rate']) + (days * rates['daily_rate'])
            else:
                return monthly_cost + (remaining_days * rates['daily_rate'])
        elif duration_days >= 7:
            weeks = duration_days // 7
            days = duration_days % 7
            return (weeks * rates['weekly_rate']) + (days * rates['daily_rate'])
        else:
            return duration_days * rates['daily_rate']
    
    def make_reservation(self, customer_name: str, model: str, start_date: str, duration_days: int) -> Dict:
        """
        Create a reservation and calculate the total cost.
        
        Args:
            customer_name: Name of the customer
            model: Excavator model
            start_date: Start date in YYYY-MM-DD format
            duration_days: Number of rental days
            
        Returns:
            Dictionary containing reservation details or error message
        """
        try:
            start_date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
            if start_date_obj < datetime.date.today():
                return {'status': 'error', 'message': 'Start date cannot be in the past'}
                
            cost = self.calculate_rental_cost(model, duration_days)
            if cost is None:
                return {'status': 'error', 'message': 'Invalid excavator model'}
                
            reservation_id = f"RES-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
            end_date = start_date_obj + datetime.timedelta(days=duration_days)
            
            self.reservations[reservation_id] = {
                'customer_name': customer_name,
                'model': model,
                'start_date': start_date,
                'end_date': end_date.strftime('%Y-%m-%d'),
                'duration_days': duration_days,
                'total_cost': cost,
                'status': 'confirmed'
            }
            
            return {
                'status': 'success',
                'reservation_id': reservation_id,
                'details': self.reservations[reservation_id]
            }
            
        except ValueError:
            return {'status': 'error', 'message': 'Invalid date format. Use YYYY-MM-DD'}
    
    def get_reservation(self, reservation_id: str) -> Optional[Dict]:
        """
        Retrieve reservation details by ID.
        
        Args:
            reservation_id: The reservation ID to look up
            
        Returns:
            Reservation details or None if not found
        """
        return self.reservations.get(reservation_id, None)
    
    def cancel_reservation(self, reservation_id: str) -> Dict:
        """
        Cancel an existing reservation.
        
        Args:
            reservation_id: The reservation ID to cancel
            
        Returns:
            Status dictionary indicating success or failure
        """
        if reservation_id in self.reservations:
            self.reservations[reservation_id]['status'] = 'cancelled'
            return {'status': 'success', 'message': 'Reservation cancelled'}
        return {'status': 'error', 'message': 'Reservation not found'}


# Example usage
if __name__ == "__main__":
    rental = YanmarMiniExcavatorRental()
    
    # Calculate cost example
    cost = rental.calculate_rental_cost('SV17', 10)
    print(f"Rental cost for 10 days: ${cost:.2f}")
    
    # Make reservation example
    reservation = rental.make_reservation(
        customer_name="John Doe",
        model="SV40",
        start_date="2023-12-01",
        duration_days=15
    )
    print("\nReservation result:")
    print(reservation)
    
    # Get reservation example
    if reservation['status'] == 'success':
        res_id = reservation['reservation_id']
        print("\nRetrieving reservation:")
        print(rental.get_reservation(res_id))
```
