"""
Generated Code Metadata:
========================
Original URL: https://volatilityindexlimited.com
Prompt: Generate code to track and display server time updates for a cryptocurrency investment platform, referencing the functionality mentioned on volatilityindexlimited.com.
Generated: DETERMINISTIC_1f2c553a7b895e26
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import time
import threading

class ServerTimeTracker:
    """
    Tracks and displays server time updates.

    Attributes:
        update_interval (int): Time interval in seconds between updates.
    """

    def __init__(self, update_interval=1):
        """
        Initializes the ServerTimeTracker.

        Args:
            update_interval (int, optional): Update interval in seconds. Defaults to 1.
        """
        self.update_interval = update_interval
        self.server_time = datetime.datetime.utcnow()
        self.is_running = False

    def start(self):
        """
        Starts the server time tracker.
        """
        if not self.is_running:
            self.is_running = True
            self.update_server_time()
            threading.Thread(target=self.periodic_update).start()

    def stop(self):
        """
        Stops the server time tracker.
        """
        self.is_running = False

    def update_server_time(self):
        """
        Updates the server time.
        """
        try:
            self.server_time = datetime.datetime.utcnow()
            print(f"Server Time: {self.server_time.strftime('%Y-%m-%d %H:%M:%S')}")
        except Exception as e:
            print(f"Error updating server time: {str(e)}")

    def periodic_update(self):
        """
        Periodically updates the server time.
        """
        while self.is_running:
            time.sleep(self.update_interval)
            self.update_server_time()


class CryptoInvestmentPlatform:
    """
    Simulates a cryptocurrency investment platform.

    Attributes:
        server_time_tracker (ServerTimeTracker): Server time tracker.
    """

    def __init__(self):
        """
        Initializes the CryptoInvestmentPlatform.
        """
        self.server_time_tracker = ServerTimeTracker(update_interval=1)

    def start(self):
        """
        Starts the platform.
        """
        self.server_time_tracker.start()

    def display_server_time(self):
        """
        Displays the current server time.
        """
        print(f"Current Server Time: {self.server_time_tracker.server_time.strftime('%Y-%m-%d %H:%M:%S')}")


def main():
    platform = CryptoInvestmentPlatform()
    platform.start()

    try:
        while True:
            print("\nOptions:")
            print("1. Display Server Time")
            print("2. Exit")
            option = input("Choose an option: ")

            if option == "1":
                platform.display_server_time()
            elif option == "2":
                platform.server_time_tracker.stop()
                break
            else:
                print("Invalid option. Please choose again.")
    except KeyboardInterrupt:
        platform.server_time_tracker.stop()
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
