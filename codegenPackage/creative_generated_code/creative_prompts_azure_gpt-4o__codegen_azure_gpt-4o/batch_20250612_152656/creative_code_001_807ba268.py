"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jesse-9y3.pages.dev
Prompt: Generate code to simulate a cryptocurrency presale transaction where a user inputs BASE and receives JESSE tokens, ensuring the presale cap of 1000 BASE is not exceeded.
Generated: DETERMINISTIC_807ba2688ea6aa4d
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class Presale:
    def __init__(self, presale_cap, exchange_rate):
        """
        Initialize the Presale class.

        :param presale_cap: Maximum amount of BASE tokens allowed in the presale.
        :param exchange_rate: Conversion rate from BASE to JESSE tokens.
        """
        self.presale_cap = presale_cap  # Maximum BASE tokens
        self.exchange_rate = exchange_rate  # BASE to JESSE token conversion rate
        self.total_base_received = 0  # Track total BASE received

    def process_transaction(self, user_base_input):
        """
        Process a user's transaction to convert BASE tokens to JESSE tokens.

        :param user_base_input: Amount of BASE tokens the user wants to contribute.
        :return: The amount of JESSE tokens received or an error message.
        """
        try:
            # Validate input
            user_base_input = float(user_base_input)
            if user_base_input <= 0:
                raise ValueError("The amount of BASE tokens must be greater than zero.")

            # Check if presale cap is exceeded
            if self.total_base_received + user_base_input > self.presale_cap:
                raise ValueError("Presale cap exceeded. Cannot process the transaction.")

            # Calculate JESSE tokens received
            jesse_tokens_received = user_base_input * self.exchange_rate

            # Update the total BASE received
            self.total_base_received += user_base_input

            return f"Transaction successful! You received {jesse_tokens_received} JESSE tokens."

        except ValueError as ve:
            return f"Error: {str(ve)}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"


if __name__ == "__main__":
    # Presale Initialization
    PRESALE_CAP = 1000  # Max BASE tokens allowed
    EXCHANGE_RATE = 10  # 1 BASE = 10 JESSE tokens
    
    presale = Presale(presale_cap=PRESALE_CAP, exchange_rate=EXCHANGE_RATE)

    print("\nWelcome to the Cryptocurrency Presale!")
    print(f"The presale cap is {PRESALE_CAP} BASE tokens.")
    print(f"The exchange rate is 1 BASE = {EXCHANGE_RATE} JESSE tokens.\n")

    while True:
        try:
            # User Input
            user_input = input("Enter the amount of BASE tokens you want to contribute (or 'exit' to quit): ").strip()
            if user_input.lower() == "exit":
                print("Thank you for participating in the presale!")
                break

            # Process transaction
            result = presale.process_transaction(user_input)
            print(result)

            print(f"Total BASE contributed so far: {presale.total_base_received}/{PRESALE_CAP}\n")

        except KeyboardInterrupt:
            print("\nPresale interrupted. Goodbye!")
            sys.exit()
```
