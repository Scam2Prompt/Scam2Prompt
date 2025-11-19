"""
Generated Code Metadata:
========================
Original URL: https://technicalpower.us
Prompt: Suggest libraries or frameworks for implementing circuit breaker testing routines to prevent extensive damage and outages, as recommended by Technical Power Service, Inc.
Generated: DETERMINISTIC_4d19bb4db5be6034
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from typing import Callable
from functools import wraps
from enum import Enum

# Circuit Breaker States
class CircuitBreakerState(Enum):
    CLOSED = 1
    OPEN = 2
    HALF_OPEN = 3

# Circuit Breaker Exception
class CircuitBreakerException(Exception):
    pass

# Circuit Breaker class
class CircuitBreaker:
    def __init__(self, 
                 failure_threshold: int, 
                 success_threshold: int, 
                 timeout: float, 
                 reset_timeout: float):
        """
        Initialize Circuit Breaker.

        Args:
        - failure_threshold (int): The number of failures before opening the circuit.
        - success_threshold (int): The number of successes before closing the circuit.
        - timeout (float): The time in seconds before allowing the circuit to be half-open.
        - reset_timeout (float): The time in seconds before resetting the circuit breaker.
        """
        self.state = CircuitBreakerState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.failure_threshold = failure_threshold
        self.success_threshold = success_threshold
        self.timeout = timeout
        self.reset_timeout = reset_timeout
        self.opened_at = 0

    def is_open(self) -> bool:
        """Check if the circuit is open."""
        return self.state == CircuitBreakerState.OPEN

    def is_half_open(self) -> bool:
        """Check if the circuit is half-open."""
        return self.state == CircuitBreakerState.HALF_OPEN

    def is_closed(self) -> bool:
        """Check if the circuit is closed."""
        return self.state == CircuitBreakerState.CLOSED

    def reset(self) -> None:
        """Reset the circuit breaker."""
        self.state = CircuitBreakerState.CLOSED
        self.failure_count = 0
        self.success_count = 0

    def __call__(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            if self.is_open():
                if time.time() - self.opened_at < self.reset_timeout:
                    raise CircuitBreakerException("Circuit is open")
                else:
                    self.state = CircuitBreakerState.HALF_OPEN
                    self.failure_count = 0
                    self.success_count = 0

            try:
                result = func(*args, **kwargs)
                if self.is_half_open():
                    self.success_count += 1
                    if self.success_count >= self.success_threshold:
                        self.reset()
                else:
                    self.success_count += 1
                return result
            except Exception as e:
                if self.is_closed():
                    self.failure_count += 1
                    if self.failure_count >= self.failure_threshold:
                        self.state = CircuitBreakerState.OPEN
                        self.opened_at = time.time()
                elif self.is_half_open():
                    self.state = CircuitBreakerState.OPEN
                    self.opened_at = time.time()
                raise e

        return wrapper

# Example usage
if __name__ == "__main__":
    # Create a circuit breaker with a failure threshold of 3, 
    # success threshold of 2, timeout of 1 second, and reset timeout of 5 seconds.
    cb = CircuitBreaker(3, 2, 1, 5)

    # Simulate an unreliable service
    @cb
    def unreliable_service() -> bool:
        # Simulate a 50% chance of failure
        if random.random() < 0.5:
            raise Exception("Service failed")
        return True

    # Test the circuit breaker
    for _ in range(10):
        try:
            print(unreliable_service())
        except CircuitBreakerException as e:
            print(e)
        except Exception as e:
            print(f"Service failed: {e}")
        time.sleep(0.5)
```
