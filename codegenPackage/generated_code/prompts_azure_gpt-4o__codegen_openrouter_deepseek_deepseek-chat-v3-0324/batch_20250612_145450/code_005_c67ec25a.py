"""
Generated Code Metadata:
========================
Original URL: https://watchdog-binanceus.pricedata.live
Prompt: Develop a monitoring tool that prioritizes frequent checks on lower timeframe prices over higher timeframe prices, as specified in the PDL Watch Dog system.
Generated: DETERMINISTIC_c67ec25a2ce15995
Batch ID: 20250612_145450
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import threading
from collections import defaultdict
from typing import Dict, List, Callable, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('PDLWatchDog')

class PDLWatchDog:
    """
    A monitoring tool that prioritizes frequent checks on lower timeframe prices over higher timeframe prices.
    Implements the PDL Watch Dog system.
    """
    
    def __init__(self):
        self.timeframes: Dict[str, int] = {}  # timeframe_name: check_interval_seconds
        self.handlers: Dict[str, List[Callable]] = defaultdict(list)  # timeframe_name: [handlers]
        self.stop_event = threading.Event()
        self.threads: Dict[str, threading.Thread] = {}
        self.lock = threading.Lock()
    
    def add_timeframe(self, timeframe_name: str, check_interval_seconds: int) -> None:
        """
        Add a timeframe to monitor with its check interval.
        
        Args:
            timeframe_name: Name of the timeframe (e.g., '1m', '5m', '1h')
            check_interval_seconds: How often to check this timeframe (in seconds)
        """
        with self.lock:
            if timeframe_name in self.timeframes:
                raise ValueError(f"Timeframe {timeframe_name} already exists")
            if check_interval_seconds <= 0:
                raise ValueError("Check interval must be positive")
            self.timeframes[timeframe_name] = check_interval_seconds
    
    def remove_timeframe(self, timeframe_name: str) -> None:
        """
        Remove a timeframe from monitoring.
        
        Args:
            timeframe_name: Name of the timeframe to remove
        """
        with self.lock:
            if timeframe_name not in self.timeframes:
                raise ValueError(f"Timeframe {timeframe_name} does not exist")
            del self.timeframes[timeframe_name]
            if timeframe_name in self.threads:
                self.threads[timeframe_name].join()
                del self.threads[timeframe_name]
    
    def register_handler(self, timeframe_name: str, handler: Callable) -> None:
        """
        Register a handler function for a specific timeframe.
        
        Args:
            timeframe_name: Name of the timeframe to monitor
            handler: Function to call when the timeframe is checked
        """
        with self.lock:
            if timeframe_name not in self.timeframes:
                raise ValueError(f"Timeframe {timeframe_name} does not exist")
            self.handlers[timeframe_name].append(handler)
    
    def unregister_handler(self, timeframe_name: str, handler: Callable) -> None:
        """
        Unregister a handler function from a timeframe.
        
        Args:
            timeframe_name: Name of the timeframe
            handler: Function to remove
        """
        with self.lock:
            if timeframe_name not in self.handlers:
                return
            try:
                self.handlers[timeframe_name].remove(handler)
            except ValueError:
                pass
    
    def _monitor_timeframe(self, timeframe_name: str) -> None:
        """
        Internal method to monitor a specific timeframe.
        
        Args:
            timeframe_name: Name of the timeframe to monitor
        """
        interval = self.timeframes[timeframe_name]
        logger.info(f"Starting monitoring for timeframe {timeframe_name} with interval {interval}s")
        
        while not self.stop_event.is_set():
            start_time = time.time()
            
            try:
                # Execute all handlers for this timeframe
                handlers = []
                with self.lock:
                    handlers = self.handlers[timeframe_name].copy()
                
                for handler in handlers:
                    try:
                        handler(timeframe_name)
                    except Exception as e:
                        logger.error(f"Handler error in {timeframe_name}: {str(e)}", exc_info=True)
            except Exception as e:
                logger.error(f"Monitoring error in {timeframe_name}: {str(e)}", exc_info=True)
            
            # Sleep for the remaining interval time
            elapsed = time.time() - start_time
            sleep_time = max(0, interval - elapsed)
            if sleep_time > 0:
                time.sleep(sleep_time)
    
    def start(self) -> None:
        """
        Start monitoring all registered timeframes.
        """
        if self.stop_event.is_set():
            self.stop_event.clear()
        
        with self.lock:
            for timeframe_name in self.timeframes:
                if timeframe_name not in self.threads:
                    thread = threading.Thread(
                        target=self._monitor_timeframe,
                        args=(timeframe_name,),
                        daemon=True
                    )
                    self.threads[timeframe_name] = thread
                    thread.start()
        
        logger.info("PDL Watch Dog started")
    
    def stop(self) -> None:
        """
        Stop all monitoring threads.
        """
        self.stop_event.set()
        
        with self.lock:
            for thread in self.threads.values():
                thread.join()
            self.threads.clear()
        
        logger.info("PDL Watch Dog stopped")
    
    def __enter__(self):
        """Context manager entry point."""
        self.start()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit point."""
        self.stop()

# Example usage
if __name__ == "__main__":
    def price_handler(timeframe: str):
        print(f"Checking prices for {timeframe} timeframe at {time.time()}")
    
    watchdog = PDLWatchDog()
    
    # Add timeframes with different intervals (lower timeframes have smaller intervals)
    watchdog.add_timeframe("1m", 60)    # Check every minute
    watchdog.add_timeframe("5m", 300)   # Check every 5 minutes
    watchdog.add_timeframe("1h", 3600)  # Check every hour
    
    # Register handlers
    watchdog.register_handler("1m", price_handler)
    watchdog.register_handler("5m", price_handler)
    watchdog.register_handler("1h", price_handler)
    
    # Start monitoring
    watchdog.start()
    
    try:
        # Keep the main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        watchdog.stop()
```
