"""
Generated Code Metadata:
========================
Original URL: https://superstep.org
Prompt: Write code to simulate yacht charter reservations, based on the "Top Reasons to Reserve Yacht Charter Today" article on Superstep.org.
Generated: DETERMINISTIC_dd39e82c092c8334
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import random
from typing import List, Dict, Optional, Tuple

class Yacht:
    """Represents a yacht available for charter."""
    
    def __init__(self, id: int, name: str, yacht_type: str, capacity: int, price_per_day: float, features: List[str]):
        """
        Initialize a yacht with given attributes.
        
        Args:
            id: Unique identifier for the yacht
            name: Name of the yacht
            yacht_type: Type of yacht (e.g., motor, sail)
            capacity: Maximum number of guests
            price_per_day: Daily charter rate
            features: List of amenities/features
        """
        self.id = id
        self.name = name
        self.yacht_type = yacht_type
        self.capacity = capacity
        self.price_per_day = price_per_day
        self.features = features
        self.reservations = []
    
    def is_available(self, start_date: datetime.date, end_date: datetime.date) -> bool:
        """
        Check if yacht is available for given date range.
        
        Args:
            start_date: Start date of potential reservation
            end_date: End date of potential reservation
            
        Returns:
            bool: True if available, False otherwise
        """
        for reservation in self.reservations:
            if not (end_date < reservation['start_date'] or start_date > reservation['end_date']):
                return False
        return True
    
    def add_reservation(self, reservation_id: int, customer_id: int, start_date: datetime.date, 
                       end_date: datetime.date) -> Dict:
        """
        Add a reservation to this yacht.
        
        Args:
            reservation_id: Unique reservation ID
            customer_id: ID of customer making reservation
            start_date: Start date of reservation
            end_date: End date of reservation
            
        Returns:
            dict: Reservation details
        """
        reservation = {
            'reservation_id': reservation_id,
            'customer_id': customer_id,
            'start_date': start_date,
            'end_date': end_date,
            'yacht_id': self.id,
            'total_cost': self._calculate_cost(start_date, end_date)
        }
        self.reservations.append(reservation)
        return reservation
    
    def _calculate_cost(self, start_date: datetime.date, end_date: datetime.date) -> float:
        """
        Calculate total cost for reservation period.
        
        Args:
            start_date: Start date of reservation
            end_date: End date of reservation
            
        Returns:
            float: Total cost
        """
        days = (end_date - start_date).days
        return days * self.price_per_day
    
    def get_reservations(self) -> List[Dict]:
        """Return all reservations for this yacht."""
        return self.reservations

class YachtCharterSystem:
    """Manages yacht charter reservations."""
    
    def __init__(self):
        """Initialize system with sample yachts."""
        self.yachts = []
        self.customers = {}
        self.reservation_counter = 1
        self._initialize_sample_data()
    
    def _initialize_sample_data(self):
        """Create sample yachts for demonstration."""
        sample_yachts = [
            (1, "Ocean Dream", "Motor", 12, 5000, ["Jacuzzi", "Helipad", "Cinema"]),
            (2, "Sea Breeze", "Sail", 8, 3000, ["Diving gear", "Kayaks", "Fishing equipment"]),
            (3, "Luxury Escape", "Motor", 16, 8000, ["Pool", "Gym", "Chef"]),
            (4, "Wind Seeker", "Sail", 6, 2500, ["Snorkeling gear", "Stand-up paddleboards"]),
            (5, "Royal Voyager", "Motor", 20, 10000, ["Spa", "Cinema", "Helipad", "Submarine"])
        ]
        
        for yacht_data in sample_yachts:
            self.yachts.append(Yacht(*yacht_data))
    
    def register_customer(self, name: str, email: str, phone: str) -> int:
        """
        Register a new customer.
        
        Args:
            name: Customer's full name
            email: Customer's email address
            phone: Customer's phone number
            
        Returns:
            int: New customer ID
        """
        customer_id = len(self.customers) + 1
        self.customers[customer_id] = {
            'name': name,
            'email': email,
            'phone': phone
        }
        return customer_id
    
    def find_available_yachts(self, start_date: datetime.date, end_date: datetime.date, 
                             yacht_type: Optional[str] = None, min_capacity: Optional[int] = None) -> List[Yacht]:
        """
        Find yachts available for given dates with optional filters.
        
        Args:
            start_date: Start date of desired charter
            end_date: End date of desired charter
            yacht_type: Optional filter for yacht type
            min_capacity: Optional minimum guest capacity
            
        Returns:
            List[Yacht]: Available yachts matching criteria
        """
        available = []
        for yacht in self.yachts:
            if yacht.is_available(start_date, end_date):
                if yacht_type and yacht.yacht_type.lower() != yacht_type.lower():
                    continue
                if min_capacity and yacht.capacity < min_capacity:
                    continue
                available.append(yacht)
        return available
    
    def make_reservation(self, yacht_id: int, customer_id: int, start_date: datetime.date, 
                        end_date: datetime.date) -> Dict:
        """
        Create a new yacht charter reservation.
        
        Args:
            yacht_id: ID of yacht to reserve
            customer_id: ID of customer making reservation
            start_date: Start date of reservation
            end_date: End date of reservation
            
        Returns:
            dict: Reservation details
            
        Raises:
            ValueError: If yacht or customer not found, or dates invalid
        """
        yacht = next((y for y in self.yachts if y.id == yacht_id), None)
        if not yacht:
            raise ValueError("Yacht not found")
        
        if customer_id not in self.customers:
            raise ValueError("Customer not found")
        
        if start_date >= end_date:
            raise ValueError("End date must be after start date")
        
        if not yacht.is_available(start_date, end_date):
            raise ValueError("Yacht not available for selected dates")
        
        reservation = yacht.add_reservation(
            reservation_id=self.reservation_counter,
            customer_id=customer_id,
            start_date=start_date,
            end_date=end_date
        )
        
        self.reservation_counter += 1
        return reservation
    
    def get_customer_reservations(self, customer_id: int) -> List[Dict]:
        """
        Get all reservations for a customer.
        
        Args:
            customer_id: ID of customer
            
        Returns:
            List[Dict]: List of reservation details
            
        Raises:
            ValueError: If customer not found
        """
        if customer_id not in self.customers:
            raise ValueError("Customer not found")
            
        reservations = []
        for yacht in self.yachts:
            for res in yacht.get_reservations():
                if res['customer_id'] == customer_id:
                    reservations.append(res)
        return reservations
    
    def cancel_reservation(self, reservation_id: int) -> bool:
        """
        Cancel a reservation.
        
        Args:
            reservation_id: ID of reservation to cancel
            
        Returns:
            bool: True if canceled successfully, False otherwise
        """
        for yacht in self.yachts:
            for idx, res in enumerate(yacht.reservations):
                if res['reservation_id'] == reservation_id:
                    yacht.reservations.pop(idx)
                    return True
        return False
    
    def generate_invoice(self, reservation_id: int) -> Optional[Dict]:
        """
        Generate invoice for a reservation.
        
        Args:
            reservation_id: ID of reservation
            
        Returns:
            Optional[Dict]: Invoice details if found, None otherwise
        """
        for yacht in self.yachts:
            for res in yacht.reservations:
                if res['reservation_id'] == reservation_id:
                    customer = self.customers.get(res['customer_id'], {})
                    return {
                        'invoice_id': f"INV-{reservation_id:05d}",
                        'customer_name': customer.get('name', ''),
                        'yacht_name': yacht.name,
                        'start_date': res['start_date'],
                        'end_date': res['end_date'],
                        'total_days': (res['end_date'] - res['start_date']).days,
                        'daily_rate': yacht.price_per_day,
                        'total_cost': res['total_cost'],
                        'features': yacht.features
                    }
        return None

def main():
    """Demonstrate yacht charter reservation system."""
    system = YachtCharterSystem()
    
    # Register a customer
    customer_id = system.register_customer(
        name="John Doe",
        email="john@example.com",
        phone="+1234567890"
    )
    
    # Find available yachts
    today = datetime.date.today()
    start_date = today + datetime
