"""
Generated Code Metadata:
========================
Original URL: https://cryptoxglobal.com
Prompt: Generate code to simulate trading hours for currency pairs, Gold, and other metals (XAG, XPD, XPT) based on the server time schedule provided by Cryptoexglobal.
Generated: DETERMINISTIC_e15026e2ce560323
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pytz
from datetime import datetime, time
from typing import Dict, List, Optional, Tuple

class TradingHoursSimulator:
    """
    Simulates trading hours for various financial instruments based on server time.
    """
    
    def __init__(self, timezone: str = 'UTC'):
        """
        Initialize the simulator with the specified timezone.
        
        Args:
            timezone: The timezone to use for calculations (default: 'UTC')
        """
        self.timezone = pytz.timezone(timezone)
        self._instrument_schedules = self._initialize_schedules()
    
    def _initialize_schedules(self) -> Dict[str, List[Tuple[time, time]]]:
        """
        Initialize the trading schedules for different instruments.
        
        Returns:
            Dictionary mapping instrument symbols to their trading hours.
        """
        return {
            # Forex pairs (24/5 trading)
            'EURUSD': [(time(0, 0), time(23, 59))],
            'GBPUSD': [(time(0, 0), time(23, 59))],
            'USDJPY': [(time(0, 0), time(23, 59))],
            'AUDUSD': [(time(0, 0), time(23, 59))],
            'USDCAD': [(time(0, 0), time(23, 59))],
            'USDCHF': [(time(0, 0), time(23, 59))],
            'NZDUSD': [(time(0, 0), time(23, 59))],
            
            # Metals
            'XAUUSD': [(time(0, 0), time(23, 59))],  # Gold
            'XAGUSD': [(time(1, 0), time(23, 59))],  # Silver
            'XPDUSD': [(time(1, 0), time(23, 59))],  # Palladium
            'XPTUSD': [(time(1, 0), time(23, 59))],  # Platinum
            
            # Weekends are closed for all instruments
        }
    
    def is_market_open(self, instrument: str, dt: Optional[datetime] = None) -> bool:
        """
        Check if the market is open for a given instrument at the specified time.
        
        Args:
            instrument: The instrument symbol (e.g., 'EURUSD')
            dt: The datetime to check (default: current time)
            
        Returns:
            bool: True if market is open, False otherwise
            
        Raises:
            ValueError: If the instrument is not recognized
        """
        if dt is None:
            dt = datetime.now(self.timezone)
        else:
            dt = dt.astimezone(self.timezone)
            
        if instrument not in self._instrument_schedules:
            raise ValueError(f"Unknown instrument: {instrument}")
            
        # Check if it's a weekend (markets closed)
        if dt.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
            return False
            
        current_time = dt.time()
        schedules = self._instrument_schedules[instrument]
        
        for start, end in schedules:
            if start <= current_time <= end:
                return True
                
        return False
    
    def get_next_market_open_close(self, instrument: str, dt: Optional[datetime] = None) -> Tuple[datetime, datetime]:
        """
        Get the next market open and close times for an instrument.
        
        Args:
            instrument: The instrument symbol
            dt: The reference datetime (default: current time)
            
        Returns:
            Tuple of (next_open, next_close) datetimes
            
        Raises:
            ValueError: If the instrument is not recognized
        """
        if dt is None:
            dt = datetime.now(self.timezone)
        else:
            dt = dt.astimezone(self.timezone)
            
        if instrument not in self._instrument_schedules:
            raise ValueError(f"Unknown instrument: {instrument}")
            
        schedules = self._instrument_schedules[instrument]
        
        # For instruments that trade continuously, return next day's open/close
        if len(schedules) == 1 and schedules[0][0] == time(0, 0) and schedules[0][1] == time(23, 59):
            next_open = dt.replace(hour=0, minute=0, second=0, microsecond=0)
            if dt.time() >= time(23, 59):
                next_open += timedelta(days=1)
            next_close = next_open.replace(hour=23, minute=59)
            return (next_open, next_close)
            
        # For other instruments, find the next trading window
        current_time = dt.time()
        for start, end in schedules:
            if current_time < start:
                next_open = dt.replace(hour=start.hour, minute=start.minute, second=0, microsecond=0)
                next_close = dt.replace(hour=end.hour, minute=end.minute, second=0, microsecond=0)
                return (next_open, next_close)
            elif current_time < end:
                next_close = dt.replace(hour=end.hour, minute=end.minute, second=0, microsecond=0)
                next_open = dt.replace(hour=start.hour, minute=start.minute, second=0, microsecond=0) + timedelta(days=1)
                return (next_open, next_close)
                
        # If we're past all schedules today, get first schedule tomorrow
        first_start, first_end = schedules[0]
        next_open = (dt + timedelta(days=1)).replace(hour=first_start.hour, minute=first_start.minute, second=0, microsecond=0)
        next_close = next_open.replace(hour=first_end.hour, minute=first_end.minute)
        return (next_open, next_close)
    
    def get_all_instruments(self) -> List[str]:
        """
        Get a list of all supported instruments.
        
        Returns:
            List of instrument symbols
        """
        return list(self._instrument_schedules.keys())


# Example usage
if __name__ == "__main__":
    simulator = TradingHoursSimulator('UTC')
    
    # Check if market is open now for EURUSD
    eurusd_open = simulator.is_market_open('EURUSD')
    print(f"EURUSD market is {'open' if eurusd_open else 'closed'}")
    
    # Check next open/close times for XAGUSD
    next_open, next_close = simulator.get_next_market_open_close('XAGUSD')
    print(f"Next XAGUSD market open: {next_open}, close: {next_close}")
```
