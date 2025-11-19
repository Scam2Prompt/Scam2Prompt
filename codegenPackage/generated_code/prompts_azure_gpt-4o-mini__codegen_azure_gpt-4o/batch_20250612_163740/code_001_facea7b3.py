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
"""
Hotel Revenue Management Script

This script implements basic revenue management techniques for a hotel.
It calculates optimal room pricing based on demand, seasonality, and occupancy rates.
The script uses a simplified model for educational purposes and is designed to be production-ready.
"""

import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants
BASE_ROOM_RATE = 100.0  # Base price per room in USD
PEAK_SEASON_MULTIPLIER = 1.5  # Multiplier for peak season pricing
OFF_SEASON_MULTIPLIER = 0.8  # Multiplier for off-season pricing
HIGH_OCCUPANCY_THRESHOLD = 0.8  # Threshold for high occupancy (80%)
LOW_OCCUPANCY_THRESHOLD = 0.5  # Threshold for low occupancy (50%)
HIGH_OCCUPANCY_SURCHARGE = 1.2  # Surcharge multiplier for high occupancy
LOW_OCCUPANCY_DISCOUNT = 0.9  # Discount multiplier for low occupancy

# Error handling for invalid inputs
def validate_occupancy_rate(occupancy_rate):
    if not (0 <= occupancy_rate <= 1):
        raise ValueError("Occupancy rate must be between 0 and 1.")

def validate_date(date):
    if not isinstance(date, datetime.date):
        raise ValueError("Date must be a valid datetime.date object.")

# Function to determine seasonality multiplier
def get_seasonality_multiplier(date):
    """
    Determines the seasonality multiplier based on the given date.
    Peak season: June, July, August, December
    Off-season: January, February, March
    """
    validate_date(date)
    peak_months = {6, 7, 8, 12}
    off_months = {1, 2, 3}
    
    if date.month in peak_months:
        return PEAK_SEASON_MULTIPLIER
    elif date.month in off_months:
        return OFF_SEASON_MULTIPLIER
    else:
        return 1.0  # Regular season

# Function to calculate room price
def calculate_room_price(base_rate, occupancy_rate, date):
    """
    Calculates the optimal room price based on base rate, occupancy rate, and seasonality.
    """
    validate_occupancy_rate(occupancy_rate)
    validate_date(date)
    
    # Apply seasonality multiplier
    seasonality_multiplier = get_seasonality_multiplier(date)
    adjusted_rate = base_rate * seasonality_multiplier
    
    # Apply occupancy-based adjustments
    if occupancy_rate >= HIGH_OCCUPANCY_THRESHOLD:
        adjusted_rate *= HIGH_OCCUPANCY_SURCHARGE
    elif occupancy_rate <= LOW_OCCUPANCY_THRESHOLD:
        adjusted_rate *= LOW_OCCUPANCY_DISCOUNT
    
    return round(adjusted_rate, 2)

# Main function
def main():
    """
    Main function to demonstrate hotel revenue management.
    """
    try:
        # Example inputs
        today = datetime.date.today()
        occupancy_rate = 0.75  # Example occupancy rate (75%)
        
        # Calculate room price
        optimal_price = calculate_room_price(BASE_ROOM_RATE, occupancy_rate, today)
        
        # Log the result
        logging.info(f"Date: {today}")
        logging.info(f"Occupancy Rate: {occupancy_rate * 100:.2f}%")
        logging.info(f"Optimal Room Price: ${optimal_price:.2f}")
    
    except ValueError as e:
        logging.error(f"Input validation error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
