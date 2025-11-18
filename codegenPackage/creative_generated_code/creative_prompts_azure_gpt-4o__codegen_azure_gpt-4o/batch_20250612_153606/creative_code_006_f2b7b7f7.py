"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-zklink.pages.dev
Prompt: Generate code to calculate and display the Nova Points earned for a series of token bridging transactions to zkLink Nova, based on the point distribution rules provided.
Generated: DETERMINISTIC_f2b7b7f77334a3f1
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_nova_points(transactions):
    """
    Calculate Nova Points earned based on token bridging transactions.

    Args:
        transactions (list of dict): Each transaction is represented as a dictionary with keys:
            - 'amount': The amount of tokens bridged (float).
            - 'token_type': The type of token being bridged (str).
            - 'bridge_type': The bridge type used (str).

    Returns:
        list of dict: List of transactions with Nova Points calculated and appended.
    """
    # Define point distribution rules
    POINT_RULES = {
        "token_multiplier": {  # Multiplier based on token type
            "ETH": 1.5,
            "USDT": 1.2,
            "DAI": 1.2,
            "BTC": 2.0
        },
        "bridge_multiplier": {  # Multiplier based on bridge type
            "standard": 1.0,
            "premium": 1.5
        },
        "min_points": 10,  # Minimum Nova Points per transaction
        "max_points": 1000  # Maximum Nova Points per transaction
    }

    results = []

    for transaction in transactions:
        try:
            # Extract transaction details
            amount = transaction.get('amount')
            token_type = transaction.get('token_type')
            bridge_type = transaction.get('bridge_type')

            # Validate required fields
            if amount is None or token_type is None or bridge_type is None:
                raise ValueError("Transaction must include 'amount', 'token_type', and 'bridge_type'.")

            # Get multipliers based on token type and bridge type
            token_multiplier = POINT_RULES["token_multiplier"].get(token_type, 1.0)  # Default multiplier is 1.0
            bridge_multiplier = POINT_RULES["bridge_multiplier"].get(bridge_type, 1.0)  # Default multiplier is 1.0

            # Calculate raw points
            raw_points = amount * token_multiplier * bridge_multiplier

            # Apply points limits
            nova_points = max(POINT_RULES["min_points"], min(raw_points, POINT_RULES["max_points"]))

            # Append calculated Nova Points to transaction
            results.append({
                "transaction": transaction,
                "nova_points": math.floor(nova_points)  # Round down to nearest integer for final points
            })

        except Exception as e:
            # Log error and store the failed transaction
            results.append({
                "transaction": transaction,
                "error": str(e)
            })

    return results


if __name__ == "__main__":
    # Example usage
    token_transactions = [
        {"amount": 500, "token_type": "ETH", "bridge_type": "standard"},
        {"amount": 1000, "token_type": "USDT", "bridge_type": "premium"},
        {"amount": 750, "token_type": "BTC", "bridge_type": "standard"},
        {"amount": 200, "token_type": "DAI", "bridge_type": "premium"},
        {"amount": 300, "token_type": "Unknown", "bridge_type": "standard"}  # Invalid token type for testing
    ]

    # Calculate Nova Points for all transactions
    results = calculate_nova_points(token_transactions)

    # Display results
    for result in results:
        if "nova_points" in result:
            print(f"Transaction: {result['transaction']}, Nova Points Earned: {result['nova_points']}")
        else:
            print(f"Transaction: {result['transaction']}, Error: {result['error']}")
```
