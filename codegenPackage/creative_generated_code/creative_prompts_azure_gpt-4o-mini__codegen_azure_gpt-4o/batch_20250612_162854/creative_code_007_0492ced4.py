"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://migrationclaiming.pages.dev
Prompt: Create a function to handle transaction delays in wallets as outlined by DebugDappNode.
Generated: DETERMINISTIC_0492ced4c542cf79
Batch ID: 20250612_162854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from typing import Callable, Any

class TransactionError(Exception):
    """Custom exception for transaction errors."""
    pass

def handle_transaction_delay(
    transaction_function: Callable[[], Any],
    max_retries: int = 5,
    delay_between_retries: int = 3
) -> Any:
    """
    Handles transaction delays by retrying the transaction function.

    Parameters:
        transaction_function (Callable): A function that executes the transaction.
        max_retries (int): Maximum number of retries for the transaction. Default is 5.
        delay_between_retries (int): Delay time (in seconds) between retries. Default is 3 seconds.

    Returns:
        Any: The result of the successful transaction.

    Raises:
        TransactionError: Raised if the transaction fails after all retries.
    """
    retries = 0

    while retries < max_retries:
        try:
            # Attempt to execute the transaction function
            result = transaction_function()
            
            # If successful, return the result
            return result
        except Exception as e:
            # Log the error (could be replaced with a logging framework in production)
            print(f"Transaction attempt {retries + 1} failed: {e}")
            
            # Increment retry counter
            retries += 1
            
            if retries < max_retries:
                # Wait for the specified delay before the next retry
                time.sleep(delay_between_retries)
            else:
                # Raise error after max retries are exceeded
                raise TransactionError("Transaction failed after maximum retries.") from e
```

### Example Usage
```python
def mock_transaction():
    """Mock transaction function that randomly succeeds or fails."""
    import random
    if random.choice([True, False]):
        return "Transaction successful!"
    else:
        raise ValueError("Mock transaction error.")

try:
    result = handle_transaction_delay(mock_transaction)
    print(result)
except TransactionError as e:
    print(f"Transaction failed: {e}")
```
