"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bulldogito.pages.dev
Prompt: Provide an example of how to calculate the number of BULLDOGITO tokens received based on a given value in a swap transaction.
Generated: DETERMINISTIC_31dfc3dd02539ca0
Batch ID: 20250612_155855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenSwap:
    def __init__(self, exchange_rate: float):
        """
        Initializes the TokenSwap with a given exchange rate.
        
        :param exchange_rate: The number of BULLDOGITO tokens received per unit of the input token.
        """
        if exchange_rate <= 0:
            raise ValueError("Exchange rate must be greater than zero.")
        self.exchange_rate = exchange_rate

    def calculate_tokens(self, input_value: float) -> float:
        """
        Calculates the number of BULLDOGITO tokens received based on the input value.

        :param input_value: The amount of the input token being swapped.
        :return: The number of BULLDOGITO tokens received.
        """
        if input_value < 0:
            raise ValueError("Input value must be non-negative.")
        
        tokens_received = input_value * self.exchange_rate
        return tokens_received

# Example usage
if __name__ == "__main__":
    # Define an exchange rate for demonstration
    exchange_rate = 100  # 100 BULLDOGITO tokens per 1 unit of the input token
    
    try:
        swap = TokenSwap(exchange_rate)
        
        input_value = 5  # Example input value to swap
        tokens = swap.calculate_tokens(input_value)
        
        print(f"Tokens received for {input_value} input value: {tokens} BULLDOGITO tokens")
        
    except ValueError as e:
        print(f"Error: {e}")
```
