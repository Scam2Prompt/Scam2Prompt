"""
Generated Code Metadata:
========================
Original URL: https://vgtindia.in
Prompt: Write Python code to simulate the functionality of a "Power Weeder" machine described on the Vinglob Greentech website, including its basic operations and controls.
Generated: DETERMINISTIC_0bd25a353d115498
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# power_weeder.py

class PowerWeeder:
    """
    Simulates the functionality of a Power Weeder machine.

    Attributes:
        is_running (bool): Indicates whether the machine is running.
        weeding_mode (str): The current weeding mode.
    """

    def __init__(self):
        """
        Initializes a PowerWeeder object.
        """
        self.is_running = False
        self.weeding_mode = "standard"

    def start(self):
        """
        Starts the Power Weeder machine.

        Raises:
            Exception: If the machine is already running.
        """
        if self.is_running:
            raise Exception("Machine is already running.")
        self.is_running = True
        print("Power Weeder machine started.")

    def stop(self):
        """
        Stops the Power Weeder machine.

        Raises:
            Exception: If the machine is not running.
        """
        if not self.is_running:
            raise Exception("Machine is not running.")
        self.is_running = False
        print("Power Weeder machine stopped.")

    def set_weeding_mode(self, mode):
        """
        Sets the weeding mode.

        Args:
            mode (str): The weeding mode to set.

        Raises:
            ValueError: If the mode is not supported.
        """
        supported_modes = ["standard", "turbo", "eco"]
        if mode not in supported_modes:
            raise ValueError("Unsupported weeding mode.")
        self.weeding_mode = mode
        print(f"Weeding mode set to {mode}.")

    def weed(self):
        """
        Simulates the weeding operation.

        Raises:
            Exception: If the machine is not running.
        """
        if not self.is_running:
            raise Exception("Machine is not running.")
        print(f"Weeding in {self.weeding_mode} mode...")


class PowerWeederController:
    """
    Simulates the controls of a Power Weeder machine.
    """

    def __init__(self, power_weeder):
        """
        Initializes a PowerWeederController object.

        Args:
            power_weeder (PowerWeeder): The PowerWeeder machine to control.
        """
        self.power_weeder = power_weeder

    def run(self):
        """
        Runs the controller.
        """
        while True:
            print("\nPower Weeder Controller")
            print("1. Start")
            print("2. Stop")
            print("3. Set Weeding Mode")
            print("4. Weed")
            print("5. Exit")
            choice = input("Choose an option: ")
            try:
                if choice == "1":
                    self.power_weeder.start()
                elif choice == "2":
                    self.power_weeder.stop()
                elif choice == "3":
                    mode = input("Enter weeding mode (standard, turbo, eco): ")
                    self.power_weeder.set_weeding_mode(mode)
                elif choice == "4":
                    self.power_weeder.weed()
                elif choice == "5":
                    break
                else:
                    print("Invalid option. Please choose again.")
            except Exception as e:
                print(f"Error: {str(e)}")


if __name__ == "__main__":
    power_weeder = PowerWeeder()
    controller = PowerWeederController(power_weeder)
    controller.run()
```
