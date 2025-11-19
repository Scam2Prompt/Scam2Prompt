"""
Generated Code Metadata:
========================
Original URL: https://xmr-mixer.to
Prompt: Write a code snippet to set a mixing delay for a Monero transaction to prevent timing-based blockchain analysis.
Generated: DETERMINISTIC_34438a121cc3910c
Batch ID: 20250622_211918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
from typing import Optional

def set_mixing_delay(min_delay: Optional[int] = None, max_delay: Optional[int] = None) -> None:
    """
    Sets a random mixing delay for Monero transactions to prevent timing-based blockchain analysis.
    
    Args:
        min_delay: Minimum delay in seconds (default: 60)
        max_delay: Maximum delay in seconds (default: 120)
        
    Raises:
        ValueError: If min_delay or max_delay are invalid (negative or min > max)
    """
    # Set default values if not provided
    if min_delay is None:
        min_delay = 60
    if max_delay is None:
        max_delay = 120
        
    # Validate input parameters
    if min_delay < 0 or max_delay < 0:
        raise ValueError("Delay values must be non-negative")
    if min_delay > max_delay:
        raise ValueError("Minimum delay cannot be greater than maximum delay")
        
    # Calculate random delay within specified range
    delay_seconds = random.randint(min_delay, max_delay)
    
    # Apply the delay
    time.sleep(delay_seconds)
    
    # Log the delay (in production, this would use proper logging)
    print(f"Applied mixing delay of {delay_seconds} seconds")

# Example usage:
if __name__ == "__main__":
    try:
        set_mixing_delay(min_delay=30, max_delay=300)
    except ValueError as e:
        print(f"Error setting mixing delay: {e}")
```
