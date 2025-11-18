"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gominingtoken.web.app
Prompt: Write a program to simulate the creation of a GoMining digital miner, including selecting power, energy efficiency, and payment method.
Generated: DETERMINISTIC_c344559d0fc08d72
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class DigitalMiner:
    """
    A class to represent a GoMining digital miner.
    """

    def __init__(self, power: int, efficiency: float, payment_method: str):
        """
        Initialize the digital miner with power, efficiency, and payment method.
        
        :param power: Power in TH/s (terahashes per second)
        :param efficiency: Energy efficiency in W/TH (watts per terahash)
        :param payment_method: Payment method as a string (e.g., 'BTC', 'ETH', 'USDT')
        """
        self.power = power
        self.efficiency = efficiency
        self.payment_method = payment_method

    def display_miner_details(self):
        """
        Display the miner's details.
        """
        print("\nDigital Miner Details:")
        print(f"Power: {self.power} TH/s")
        print(f"Energy Efficiency: {self.efficiency} W/TH")
        print(f"Payment Method: {self.payment_method}")


def get_user_input(prompt: str, validation_fn=None):
    """
    Generic function to get input from the user with optional validation.
    
    :param prompt: Prompt to display to the user.
    :param validation_fn: Optional function to validate the input.
    :return: Validated user input.
    """
    while True:
        try:
            value = input(prompt)
            if validation_fn:
                value = validation_fn(value)  # Validate the input
            return value
        except Exception as e:
            print(f"Error: {str(e)}. Please try again.")


def validate_power(input_str):
    """
    Validate and convert input power to an integer.
    
    :param input_str: Input string
    :return: Valid integer power value
    :raises ValueError: If the input is not a positive integer
    """
    power = int(input_str)
    if power <= 0:
        raise ValueError("Power must be a positive integer.")
    return power


def validate_efficiency(input_str):
    """
    Validate and convert input efficiency to a float.
    
    :param input_str: Input string
    :return: Valid float efficiency value
    :raises ValueError: If the input is not positive
    """
    efficiency = float(input_str)
    if efficiency <= 0:
        raise ValueError("Energy efficiency must be a positive number.")
    return efficiency


def validate_payment_method(input_str):
    """
    Validate the payment method.
    
    :param input_str: Input string
    :return: Valid payment method as a string
    :raises ValueError: If the input is not in the allowed methods
    """
    allowed_methods = ['BTC', 'ETH', 'USDT']
    if input_str.upper() not in allowed_methods:
        raise ValueError(f"Payment method must be one of {', '.join(allowed_methods)}.")
    return input_str.upper()


def main():
    """
    Main function to simulate the creation of a GoMining digital miner.
    """
    print("Welcome to GoMining Digital Miner Simulator!")

    # Get power from user
    power = get_user_input("Enter miner power (in TH/s): ", validate_power)

    # Get energy efficiency from user
    efficiency = get_user_input("Enter energy efficiency (in W/TH): ", validate_efficiency)

    # Get payment method from user
    payment_method = get_user_input(
        f"Enter payment method (BTC, ETH, USDT): ", validate_payment_method
    )

    # Create the digital miner
    miner = DigitalMiner(power=power, efficiency=efficiency, payment_method=payment_method)

    # Display the miner details
    miner.display_miner_details()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        sys.exit(0)
```
