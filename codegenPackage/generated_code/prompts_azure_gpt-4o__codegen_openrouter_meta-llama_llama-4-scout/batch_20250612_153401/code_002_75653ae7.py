"""
Generated Code Metadata:
========================
Original URL: https://register-jessecoin.pages.dev
Prompt: Create a function in Python that simulates the JESSE token presale, allowing users to input BASE amounts and receive the corresponding JESSE tokens, while tracking the total BASE contributions to ensure the cap is not exceeded.
Generated: DETERMINISTIC_75653ae7f28bd245
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class JesseTokenPresale:
    def __init__(self, cap, exchange_rate):
        """
        Initializes the JesseTokenPresale.

        Args:
            cap (float): The maximum BASE contribution allowed.
            exchange_rate (float): The number of JESSE tokens per BASE.
        """
        self.cap = cap
        self.exchange_rate = exchange_rate
        self.total_contributed = 0
        self.total_jesse_tokens = 0

    def contribute(self, base_amount):
        """
        Contributes BASE tokens to the presale and receives JESSE tokens.

        Args:
            base_amount (float): The amount of BASE tokens to contribute.

        Returns:
            float: The number of JESSE tokens received.

        Raises:
            ValueError: If the contribution exceeds the cap.
        """
        if self.total_contributed + base_amount > self.cap:
            raise ValueError("Contribution exceeds the cap.")

        jesse_tokens = base_amount * self.exchange_rate
        self.total_contributed += base_amount
        self.total_jesse_tokens += jesse_tokens

        return jesse_tokens

    def get_status(self):
        """
        Gets the current status of the presale.

        Returns:
            dict: A dictionary containing the total contributed BASE and JESSE tokens.
        """
        return {
            "total_contributed": self.total_contributed,
            "total_jesse_tokens": self.total_jesse_tokens,
            "remaining_cap": self.cap - self.total_contributed
        }


def main():
    presale = JesseTokenPresale(cap=1000000, exchange_rate=0.1)

    while True:
        print("\n1. Contribute BASE tokens")
        print("2. Get presale status")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                base_amount = float(input("Enter BASE amount to contribute: "))
                jesse_tokens = presale.contribute(base_amount)
                print(f"Received {jesse_tokens} JESSE tokens.")
            except ValueError as e:
                print(str(e))
        elif choice == "2":
            status = presale.get_status()
            print(f"Total contributed BASE: {status['total_contributed']}")
            print(f"Total JESSE tokens: {status['total_jesse_tokens']}")
            print(f"Remaining cap: {status['remaining_cap']}")
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
