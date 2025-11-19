"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Create a simple revenue management tool using Excel VBA or Python, considering dynamic pricing and accommodation management strategies.
Generated: DETERMINISTIC_601df1312d917fe7
Batch ID: 20250622_204740
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
from typing import List, Dict, Optional

class RevenueManagementTool:
    """
    A simple revenue management tool with dynamic pricing and accommodation management capabilities.
    """
    
    def __init__(self):
        self.accommodations = pd.DataFrame(columns=[
            'id', 'name', 'base_price', 'capacity', 'booked', 'min_price', 'max_price'
        ])
        self.bookings = pd.DataFrame(columns=[
            'id', 'accommodation_id', 'check_in', 'check_out', 'guests', 'price', 'status'
        ])
        self.dynamic_pricing_factors = {
            'demand_factor': 1.0,
            'season_factor': 1.0,
            'lead_time_factor': 1.0
        }
        
    def add_accommodation(self, name: str, base_price: float, capacity: int,
                          min_price: float, max_price: float) -> int:
        """
        Add a new accommodation to the system.
        Returns the generated accommodation ID.
        """
        if min_price > max_price:
            raise ValueError("Minimum price cannot be greater than maximum price")
        if base_price < min_price or base_price > max_price:
            raise ValueError("Base price must be between min and max price")
            
        new_id = len(self.accommodations) + 1
        new_accommodation = pd.DataFrame([{
            'id': new_id,
            'name': name,
            'base_price': base_price,
            'capacity': capacity,
            'booked': 0,
            'min_price': min_price,
            'max_price': max_price
        }])
        
        self.accommodations = pd.concat([self.accommodations, new_accommodation], ignore_index=True)
        return new_id
    
    def update_dynamic_pricing_factors(self, demand_factor: float = None,
                                      season_factor: float = None,
                                      lead_time_factor: float = None):
        """
        Update dynamic pricing factors.
        """
        if demand_factor is not None:
            self.dynamic_pricing_factors['demand_factor'] = max(0.5, min(2.0, demand_factor))
        if season_factor is not None:
            self.dynamic_pricing_factors['season_factor'] = max(0.5, min(2.0, season_factor))
        if lead_time_factor is not None:
            self.dynamic_pricing_factors['lead_time_factor'] = max(0.5, min(2.0, lead_time_factor))
    
    def calculate_dynamic_price(self, accommodation_id: int, check_in: datetime,
                               check_out: datetime, guests: int) -> float:
        """
        Calculate dynamic price based on current factors and occupancy.
        """
        acc = self.accommodations[self.accommodations['id'] == accommodation_id].iloc[0]
        
        if guests > acc['capacity']:
            raise ValueError("Number of guests exceeds accommodation capacity")
            
        # Calculate occupancy rate
        occupancy_rate = acc['booked'] / acc['capacity']
        
        # Calculate dynamic price components
        base_price = acc['base_price']
        demand_component = base_price * (self.dynamic_pricing_factors['demand_factor'] - 1) * occupancy_rate
        season_component = base_price * (self.dynamic_pricing_factors['season_factor'] - 1)
        
        # Calculate lead time component (earlier bookings get discounts)
        lead_time = (check_in - datetime.now()).days
        lead_time_component = base_price * (1 - self.dynamic_pricing_factors['lead_time_factor']) * (1 - min(1, lead_time/30))
        
        dynamic_price = base_price + demand_component + season_component + lead_time_component
        
        # Ensure price stays within bounds
        dynamic_price = max(acc['min_price'], min(acc['max_price'], dynamic_price))
        
        return round(dynamic_price, 2)
    
    def create_booking(self, accommodation_id: int, check_in: datetime,
                      check_out: datetime, guests: int) -> Dict:
        """
        Create a new booking with dynamic pricing.
        """
        if check_in >= check_out:
            raise ValueError("Check-in date must be before check-out date")
            
        acc = self.accommodations[self.accommodations['id'] == accommodation_id].iloc[0]
        
        if acc['booked'] + guests > acc['capacity']:
            raise ValueError("Not enough capacity for this booking")
            
        price = self.calculate_dynamic_price(accommodation_id, check_in, check_out, guests)
        
        new_id = len(self.bookings) + 1
        new_booking = pd.DataFrame([{
            'id': new_id,
            'accommodation_id': accommodation_id,
            'check_in': check_in,
            'check_out': check_out,
            'guests': guests,
            'price': price,
            'status': 'confirmed'
        }])
        
        self.bookings = pd.concat([self.bookings, new_booking], ignore_index=True)
        
        # Update accommodation booked count
        self.accommodations.loc[self.accommodations['id'] == accommodation_id, 'booked'] += guests
        
        return {
            'booking_id': new_id,
            'price': price,
            'status': 'confirmed'
        }
    
    def cancel_booking(self, booking_id: int) -> None:
        """
        Cancel a booking and update accommodation availability.
        """
        booking = self.bookings[self.bookings['id'] == booking_id].iloc[0]
        
        if booking['status'] == 'cancelled':
            return
            
        self.bookings.loc[self.bookings['id'] == booking_id, 'status'] = 'cancelled'
        
        # Update accommodation booked count
        accommodation_id = booking['accommodation_id']
        guests = booking['guests']
        self.accommodations.loc[self.accommodations['id'] == accommodation_id, 'booked'] -= guests
    
    def get_occupancy_report(self, start_date: datetime, end_date: datetime) -> pd.DataFrame:
        """
        Generate occupancy report for a date range.
        """
        report = []
        current_date = start_date
        
        while current_date <= end_date:
            daily_bookings = self.bookings[
                (self.bookings['check_in'] <= current_date) & 
                (self.bookings['check_out'] > current_date) &
                (self.bookings['status'] == 'confirmed')
            ]
            
            total_capacity = self.accommodations['capacity'].sum()
            total_booked = daily_bookings['guests'].sum()
            occupancy_rate = total_booked / total_capacity if total_capacity > 0 else 0
            
            report.append({
                'date': current_date,
                'total_capacity': total_capacity,
                'total_booked': total_booked,
                'occupancy_rate': occupancy_rate
            })
            
            current_date += timedelta(days=1)
        
        return pd.DataFrame(report)
    
    def get_revenue_report(self, start_date: datetime, end_date: datetime) -> pd.DataFrame:
        """
        Generate revenue report for a date range.
        """
        relevant_bookings = self.bookings[
            (self.bookings['check_in'] >= start_date) & 
            (self.bookings['check_out'] <= end_date) &
            (self.bookings['status'] == 'confirmed')
        ]
        
        if relevant_bookings.empty:
            return pd.DataFrame(columns=['date', 'revenue', 'bookings'])
            
        # Calculate daily revenue
        revenue_data = []
        for _, booking in relevant_bookings.iterrows():
            nights = (booking['check_out'] - booking['check_in']).days
            daily_price = booking['price'] / nights if nights > 0 else booking['price']
            
            current_date = booking['check_in']
            while current_date < booking['check_out']:
                revenue_data.append({
                    'date': current_date,
                    'revenue': daily_price,
                    'bookings': 1
                })
                current_date += timedelta(days=1)
        
        revenue_df = pd.DataFrame(revenue_data)
        return revenue_df.groupby('date').agg({
            'revenue': 'sum',
            'bookings': 'sum'
        }).reset_index()
```
