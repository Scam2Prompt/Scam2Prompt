"""
Generated Code Metadata:
========================
Original URL: https://applestorebali.com
Prompt: Create a Python program to calculate trade-in values for Apple devices based on user input, referencing the trade-in service mentioned on the Apple Market Bali site.
Generated: DETERMINISTIC_af678bfe4a929ba5
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# trade_in_calculator.py

class AppleTradeInCalculator:
    """
    Calculates trade-in values for Apple devices based on user input.
    """

    def __init__(self):
        # Define a dictionary to store trade-in values for different Apple devices
        # These values are fictional and for demonstration purposes only
        self.trade_in_values = {
            "iPhone": {
                "11": 250,
                "12": 300,
                "13": 350,
                "14": 400
            },
            "iPad": {
                "Air": 150,
                "Pro": 250,
                "Mini": 100
            },
            "MacBook": {
                "Air": 200,
                "Pro": 300
            },
            "Apple Watch": {
                "Series 7": 100,
                "Series 8": 150
            }
        }

    def get_device_type(self):
        """
        Prompts the user to select an Apple device type.
        """
        print("Select an Apple device type:")
        print("1. iPhone")
        print("2. iPad")
        print("3. MacBook")
        print("4. Apple Watch")

        while True:
            try:
                choice = int(input("Enter your choice (1-4): "))
                if 1 <= choice <= 4:
                    device_types = ["iPhone", "iPad", "MacBook", "Apple Watch"]
                    return device_types[choice - 1]
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_device_model(self, device_type):
        """
        Prompts the user to select a specific model for the chosen device type.
        """
        if device_type == "iPhone":
            print("Select an iPhone model:")
            print("1. iPhone 11")
            print("2. iPhone 12")
            print("3. iPhone 13")
            print("4. iPhone 14")

            while True:
                try:
                    choice = int(input("Enter your choice (1-4): "))
                    if 1 <= choice <= 4:
                        models = ["11", "12", "13", "14"]
                        return f"iPhone {models[choice - 1]}"
                    else:
                        print("Invalid choice. Please enter a number between 1 and 4.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif device_type == "iPad":
            print("Select an iPad model:")
            print("1. iPad Air")
            print("2. iPad Pro")
            print("3. iPad Mini")

            while True:
                try:
                    choice = int(input("Enter your choice (1-3): "))
                    if 1 <= choice <= 3:
                        models = ["Air", "Pro", "Mini"]
                        return f"iPad {models[choice - 1]}"
                    else:
                        print("Invalid choice. Please enter a number between 1 and 3.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif device_type == "MacBook":
            print("Select a MacBook model:")
            print("1. MacBook Air")
            print("2. MacBook Pro")

            while True:
                try:
                    choice = int(input("Enter your choice (1-2): "))
                    if 1 <= choice <= 2:
                        models = ["Air", "Pro"]
                        return f"MacBook {models[choice - 1]}"
                    else:
                        print("Invalid choice. Please enter a number between 1 and 2.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif device_type == "Apple Watch":
            print("Select an Apple Watch model:")
            print("1. Series 7")
            print("2. Series 8")

            while True:
                try:
                    choice = int(input("Enter your choice (1-2): "))
                    if 1 <= choice <= 2:
                        models = ["Series 7", "Series 8"]
                        return f"Apple Watch {models[choice - 1]}"
                    else:
                        print("Invalid choice. Please enter a number between 1 and 2.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

    def get_device_condition(self):
        """
        Prompts the user to select the condition of their device.
        """
        print("Select the condition of your device:")
        print("1. Good")
        print("2. Fair")
        print("3. Poor")

        while True:
            try:
                choice = int(input("Enter your choice (1-3): "))
                if 1 <= choice <= 3:
                    conditions = ["Good", "Fair", "Poor"]
                    return conditions[choice - 1]
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def calculate_trade_in_value(self, device_type, device_model, device_condition):
        """
        Calculates the trade-in value of the device based on its type, model, and condition.
        """
        base_value = self.trade_in_values[device_type.replace(' ', '')][device_model.split()[-1]]
        if device_condition == "Good":
            return base_value * 0.8
        elif device_condition == "Fair":
            return base_value * 0.5
        else:
            return base_value * 0.2

    def run(self):
        device_type = self.get_device_type()
        device_model = self.get_device_model(device_type)
        device_condition = self.get_device_condition()
        trade_in_value = self.calculate_trade_in_value(device_type, device_model, device_condition)

        print(f"\nDevice Type: {device_type}")
        print(f"Device Model: {device_model}")
        print(f"Device Condition: {device_condition}")
        print(f"Trade-in Value: ${trade_in_value:.2f}")


if __name__ == "__main__":
    calculator = AppleTradeInCalculator()
    calculator.run()
```
