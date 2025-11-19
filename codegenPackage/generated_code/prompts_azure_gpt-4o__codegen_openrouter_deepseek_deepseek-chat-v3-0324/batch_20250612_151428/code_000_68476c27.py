"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Write Python code to simulate a booking system for hiring police uniforms and replica firearms, incorporating a security deposit and credit card validation as described on the Powered Production Film Services website.
Generated: DETERMINISTIC_68476c27c07004ca
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

class BookingSystem:
    """
    A booking system for hiring police uniforms and replica firearms.
    Handles inventory management, bookings, security deposits, and credit card validation.
    """
    
    def __init__(self):
        self.uniforms_inventory: Dict[str, int] = {
            "Standard Police Uniform": 10,
            "SWAT Uniform": 5,
            "Detective Outfit": 8
        }
        
        self.firearms_inventory: Dict[str, int] = {
            "Replica Handgun": 15,
            "Replica Rifle": 7,
            "Replica Shotgun": 5
        }
        
        self.bookings: List[Dict] = []
        self.security_deposit_amount: float = 200.00  # Default security deposit
    
    def validate_credit_card(self, card_number: str, expiry_date: str, cvv: str) -> bool:
        """
        Validates credit card details.
        
        Args:
            card_number: Credit card number (16 digits)
            expiry_date: Expiry date in MM/YY format
            cvv: 3 or 4 digit CVV
            
        Returns:
            bool: True if card is valid, False otherwise
        """
        # Validate card number (16 digits)
        if not re.fullmatch(r'^\d{16}$', card_number):
            return False
        
        # Validate expiry date
        try:
            month, year = expiry_date.split('/')
            month = int(month)
            year = int(year)
            
            if month < 1 or month > 12:
                return False
                
            current_year = datetime.now().year % 100
            current_month = datetime.now().month
            
            if year < current_year or (year == current_year and month < current_month):
                return False
        except:
            return False
        
        # Validate CVV (3 or 4 digits)
        if not re.fullmatch(r'^\d{3,4}$', cvv):
            return False
            
        return True
    
    def check_availability(self, item_type: str, item_name: str, quantity: int, start_date: str, end_date: str) -> bool:
        """
        Checks if requested items are available for the given dates.
        
        Args:
            item_type: 'uniform' or 'firearm'
            item_name: Name of the item
            quantity: Number of items requested
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            
        Returns:
            bool: True if available, False otherwise
        """
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
            
            if start > end:
                return False
                
            inventory = self.uniforms_inventory if item_type == "uniform" else self.firearms_inventory
            
            if item_name not in inventory or inventory[item_name] < quantity:
                return False
                
            # Check for overlapping bookings
            for booking in self.bookings:
                if booking["item_name"] == item_name:
                    booking_start = datetime.strptime(booking["start_date"], "%Y-%m-%d")
                    booking_end = datetime.strptime(booking["end_date"], "%Y-%m-%d")
                    
                    if not (end < booking_start or start > booking_end):
                        available = booking["available_quantity"]
                        if available < quantity:
                            return False
                            
            return True
        except ValueError:
            return False
    
    def create_booking(
        self,
        customer_name: str,
        customer_email: str,
        item_type: str,
        item_name: str,
        quantity: int,
        start_date: str,
        end_date: str,
        card_number: str,
        expiry_date: str,
        cvv: str
    ) -> Tuple[bool, str]:
        """
        Creates a new booking with security deposit and credit card validation.
        
        Args:
            customer_name: Name of the customer
            customer_email: Email of the customer
            item_type: 'uniform' or 'firearm'
            item_name: Name of the item
            quantity: Number of items
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            card_number: Credit card number for deposit
            expiry_date: Card expiry in MM/YY format
            cvv: Card CVV
            
        Returns:
            Tuple: (success: bool, message: str)
        """
        # Validate inputs
        if not all([customer_name, customer_email, item_type, item_name, quantity > 0, start_date, end_date]):
            return False, "Missing required fields"
            
        if item_type not in ["uniform", "firearm"]:
            return False, "Invalid item type"
            
        if not self.validate_credit_card(card_number, expiry_date, cvv):
            return False, "Invalid credit card details"
            
        if not self.check_availability(item_type, item_name, quantity, start_date, end_date):
            return False, "Requested items not available for the selected dates"
            
        # Calculate rental period and cost
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
            rental_days = (end - start).days + 1
        except ValueError:
            return False, "Invalid date format"
            
        # Create booking record (in a real system, this would charge the card)
        booking_id = f"BK-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        booking = {
            "booking_id": booking_id,
            "customer_name": customer_name,
            "customer_email": customer_email,
            "item_type": item_type,
            "item_name": item_name,
            "quantity": quantity,
            "start_date": start_date,
            "end_date": end_date,
            "security_deposit": self.security_deposit_amount * quantity,
            "card_last_four": card_number[-4:],
            "booking_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "confirmed"
        }
        
        self.bookings.append(booking)
        
        # Update inventory (simplified - in real system would track per booking)
        if item_type == "uniform":
            self.uniforms_inventory[item_name] -= quantity
        else:
            self.firearms_inventory[item_name] -= quantity
            
        return True, f"Booking {booking_id} confirmed. Security deposit of ${booking['security_deposit']:.2f} will be held."
    
    def return_items(self, booking_id: str) -> Tuple[bool, str]:
        """
        Processes item returns and releases security deposit.
        
        Args:
            booking_id: ID of the booking to return
            
        Returns:
            Tuple: (success: bool, message: str)
        """
        booking = next((b for b in self.bookings if b["booking_id"] == booking_id), None)
        
        if not booking:
            return False, "Booking not found"
            
        if booking["status"] == "returned":
            return False, "Items already returned"
            
        # In a real system, this would process the deposit refund
        booking["status"] = "returned"
        booking["return_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Restore inventory
        if booking["item_type"] == "uniform":
            self.uniforms_inventory[booking["item_name"]] += booking["quantity"]
        else:
            self.firearms_inventory[booking["item_name"]] += booking["quantity"]
            
        return True, f"Items returned. Security deposit of ${booking['security_deposit']:.2f} will be refunded."
    
    def get_available_items(self, item_type: str) -> Dict[str, int]:
        """
        Returns available items of specified type.
        
        Args:
            item_type: 'uniform' or 'firearm'
            
        Returns:
            Dict: Item names and available quantities
        """
        if item_type == "uniform":
            return self.uniforms_inventory.copy()
        elif item_type == "firearm":
            return self.firearms_inventory.copy()
        else:
            return {}
```
