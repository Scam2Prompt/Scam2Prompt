"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Write a Python script that implements revenue management techniques for a hotel, based on the principles taught in the International Tourism & Hospitality Management course at Hampton's.
Generated: DETERMINISTIC_facea7b39b66392b
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class HotelRevenueManager:
    """
    A class to manage hotel revenue using dynamic pricing, demand forecasting, and inventory control.
    Implements revenue management techniques taught in International Tourism & Hospitality Management.
    """

    def __init__(self, room_types: List[str], base_prices: Dict[str, float], total_rooms: Dict[str, int]):
        """
        Initialize the revenue manager with room types, base prices, and inventory.

        Args:
            room_types: List of room type names (e.g., ['Standard', 'Deluxe', 'Suite'])
            base_prices: Dictionary mapping room types to their base prices
            total_rooms: Dictionary mapping room types to total available rooms
        """
        self.room_types = room_types
        self.base_prices = base_prices
        self.total_rooms = total_rooms
        self.available_rooms = total_rooms.copy()
        self.bookings = pd.DataFrame(columns=['room_type', 'check_in', 'check_out', 'price', 'customer_id'])
        self.demand_history = pd.DataFrame(columns=['date', 'room_type', 'demand', 'price'])

        # Validate inputs
        if not all(rt in base_prices for rt in room_types):
            raise ValueError("All room types must have base prices")
        if not all(rt in total_rooms for rt in room_types):
            raise ValueError("All room types must have room counts")

    def make_booking(self, room_type: str, check_in: str, check_out: str, customer_id: str) -> Optional[float]:
        """
        Process a booking request and return the price if successful.

        Args:
            room_type: Type of room being booked
            check_in: Check-in date (YYYY-MM-DD)
            check_out: Check-out date (YYYY-MM-DD)
            customer_id: Unique customer identifier

        Returns:
            Price if booking is successful, None otherwise
        """
        try:
            # Validate room type
            if room_type not in self.room_types:
                logger.warning(f"Invalid room type: {room_type}")
                return None

            # Convert dates to datetime objects
            ci_date = datetime.strptime(check_in, '%Y-%m-%d').date()
            co_date = datetime.strptime(check_out, '%Y-%m-%d').date()

            # Check date validity
            if ci_date >= co_date:
                logger.warning(f"Invalid dates: check-in {check_in} must be before check-out {check_out}")
                return None

            # Check room availability
            if not self._check_availability(room_type, ci_date, co_date):
                logger.info(f"No availability for {room_type} from {check_in} to {check_out}")
                return None

            # Calculate dynamic price
            price = self._calculate_dynamic_price(room_type, ci_date, co_date)

            # Record booking
            new_booking = {
                'room_type': room_type,
                'check_in': ci_date,
                'check_out': co_date,
                'price': price,
                'customer_id': customer_id
            }
            self.bookings = pd.concat([self.bookings, pd.DataFrame([new_booking])], ignore_index=True)

            # Update inventory
            self._update_inventory(room_type, ci_date, co_date)

            # Update demand history
            self._update_demand_history(room_type, ci_date, co_date, price)

            logger.info(f"Booking confirmed for {room_type} at ${price:.2f}")
            return price

        except Exception as e:
            logger.error(f"Error processing booking: {str(e)}")
            return None

    def _check_availability(self, room_type: str, check_in: datetime.date, check_out: datetime.date) -> bool:
        """
        Check room availability for given dates.

        Args:
            room_type: Type of room to check
            check_in: Check-in date
            check_out: Check-out date

        Returns:
            True if room is available, False otherwise
        """
        # Get all bookings for this room type
        room_bookings = self.bookings[self.bookings['room_type'] == room_type]

        # Check for each day in the stay
        current_date = check_in
        while current_date < check_out:
            # Count bookings overlapping with this date
            overlapping = room_bookings[
                (room_bookings['check_in'] <= current_date) & 
                (room_bookings['check_out'] > current_date)
            ]
            if len(overlapping) >= self.total_rooms[room_type]:
                return False
            current_date += timedelta(days=1)

        return True

    def _calculate_dynamic_price(self, room_type: str, check_in: datetime.date, check_out: datetime.date) -> float:
        """
        Calculate dynamic price based on demand, seasonality, and remaining inventory.

        Args:
            room_type: Type of room being priced
            check_in: Check-in date
            check_out: Check-out date

        Returns:
            Calculated price for the stay
        """
        base_price = self.base_prices[room_type]
        duration = (check_out - check_in).days

        # Get current bookings for this period
        current_bookings = self.bookings[
            (self.bookings['room_type'] == room_type) &
            (self.bookings['check_in'] < check_out) &
            (self.bookings['check_out'] > check_in)
        ]

        # Calculate occupancy rate
        max_possible = self.total_rooms[room_type] * duration
        current_booked = len(current_bookings)
        occupancy_rate = current_booked / max_possible if max_possible > 0 else 0

        # Price adjustment factors
        lead_time_factor = self._calculate_lead_time_factor(check_in)
        seasonality_factor = self._calculate_seasonality_factor(check_in)
        demand_factor = self._calculate_demand_factor(room_type, check_in, check_out)

        # Calculate final price
        price = base_price * (1 + occupancy_rate) * lead_time_factor * seasonality_factor * demand_factor
        return round(price, 2)

    def _calculate_lead_time_factor(self, check_in: datetime.date) -> float:
        """
        Calculate price adjustment based on how far in advance the booking is made.
        """
        days_until_checkin = (check_in - datetime.now().date()).days
        if days_until_checkin > 60:  # Very early booking
            return 0.9
        elif days_until_checkin > 30:  # Early booking
            return 1.0
        elif days_until_checkin > 14:  # Moderate lead time
            return 1.1
        elif days_until_checkin > 7:  # Short lead time
            return 1.2
        else:  # Last minute
            return 1.3

    def _calculate_seasonality_factor(self, date: datetime.date) -> float:
        """
        Calculate seasonal price adjustment.
        """
        month = date.month
        # Example seasonal factors (adjust based on actual hotel location)
        if month in [6, 7, 8]:  # Peak summer
            return 1.4
        elif month in [12, 1, 2]:  # Winter holidays
            return 1.3
        elif month in [3, 4, 5, 9, 10, 11]:  # Shoulder seasons
            return 1.1
        else:
            return 1.0

    def _calculate_demand_factor(self, room_type: str, check_in: datetime.date, check_out: datetime.date) -> float:
        """
        Calculate price adjustment based on historical demand patterns.
        """
        # Simple implementation - in production would use more sophisticated forecasting
        try:
            # Get historical demand for similar periods
            historical = self.demand_history[
                (self.demand_history['room_type'] == room_type) &
                (self.demand_history['date'].dt.month == check_in.month)
            ]
            if not historical.empty:
                avg_demand = historical['demand'].mean()
                max_demand = historical['demand'].max()
                if max_demand > 0:
                    return 1 + (avg_demand / max_demand) * 0.5  # Scale factor
        except Exception as e:
            logger.warning(f"Error calculating demand factor: {str(e)}")
        
        return 1.0

    def _update_inventory(self, room_type: str, check_in: datetime.date, check_out: datetime.date):
        """
        Update available room counts after a successful booking.
        """
        # In our current implementation, availability is checked dynamically in _check_availability
        # This method would be used in a system with pre-allocated inventory
        pass

    def _update_demand_history(self, room_type: str, check_in:
