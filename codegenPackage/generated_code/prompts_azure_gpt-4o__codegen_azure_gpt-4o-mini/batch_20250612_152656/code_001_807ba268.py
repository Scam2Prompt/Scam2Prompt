"""
Generated Code Metadata:
========================
Original URL: https://jesse-9y3.pages.dev
Prompt: Generate code to simulate a cryptocurrency presale transaction where a user inputs BASE and receives JESSE tokens, ensuring the presale cap of 1000 BASE is not exceeded.
Generated: DETERMINISTIC_807ba2688ea6aa4d
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PresaleError(Exception):
    """Custom exception for presale errors."""
    pass

class Presale:
    def __init__(self, cap: float):
        """
        Initialize the presale with a specified cap.

        :param cap: The maximum amount of BASE that can be raised in the presale.
        """
        self.cap = cap
        self.total_base_received = 0.0

    def buy_tokens(self, base_amount: float) -> float:
        """
        Simulate a purchase of JESSE tokens with BASE.

        :param base_amount: The amount of BASE the user wants to spend.
        :return: The amount of JESSE tokens received.
        :raises PresaleError: If the presale cap is exceeded or if the input is invalid.
        """
        if base_amount <= 0:
            raise PresaleError("The amount of BASE must be greater than zero.")
        
        if self.total_base_received + base_amount > self.cap:
            raise PresaleError("Presale cap exceeded. Cannot accept this transaction.")

        # Assuming a fixed exchange rate of 1 BASE = 10 JESSE tokens
        jes_tokens_received = base_amount * 10
        self.total_base_received += base_amount

        return jes_tokens_received

def main():
    presale_cap = 1000.0  # Presale cap in BASE
    presale = Presale(presale_cap)

    while True:
        try:
            # User input for BASE amount
            user_input = input("Enter the amount of BASE to spend (or 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Exiting the presale.")
                break

            base_amount = float(user_input)
            jes_tokens = presale.buy_tokens(base_amount)
            print(f"Transaction successful! You received {jes_tokens} JESSE tokens.")
            print(f"Total BASE received so far: {presale.total_base_received}/{presale.cap}")

        except ValueError:
            print("Invalid input. Please enter a numeric value for BASE.")
        except PresaleError as e:
            print(f"Transaction failed: {e}")

if __name__ == "__main__":
    main()
```
