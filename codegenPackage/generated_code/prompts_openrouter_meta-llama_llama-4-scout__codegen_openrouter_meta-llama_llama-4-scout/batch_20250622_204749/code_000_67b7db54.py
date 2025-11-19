"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: "Write a Python script to manage traffic signal installations for an electrical contractor like E.C. Power & Lighting Ltd."
Generated: DETERMINISTIC_67b7db54fbd7dee4
Batch ID: 20250622_204749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# traffic_signal_manager.py

class TrafficSignal:
    def __init__(self, signal_id, location, installation_date):
        """
        Initialize a TrafficSignal object.

        Args:
            signal_id (str): Unique identifier for the traffic signal.
            location (str): Location of the traffic signal.
            installation_date (str): Date of installation in YYYY-MM-DD format.
        """
        self.signal_id = signal_id
        self.location = location
        self.installation_date = installation_date
        self.status = "Installed"

    def __str__(self):
        return f"Traffic Signal {self.signal_id} at {self.location}"


class TrafficSignalManager:
    def __init__(self):
        """
        Initialize a TrafficSignalManager object.
        """
        self.traffic_signals = {}

    def add_traffic_signal(self, signal_id, location, installation_date):
        """
        Add a new traffic signal to the manager.

        Args:
            signal_id (str): Unique identifier for the traffic signal.
            location (str): Location of the traffic signal.
            installation_date (str): Date of installation in YYYY-MM-DD format.

        Raises:
            ValueError: If a traffic signal with the same ID already exists.
        """
        if signal_id in self.traffic_signals:
            raise ValueError("Traffic signal with this ID already exists")
        self.traffic_signals[signal_id] = TrafficSignal(signal_id, location, installation_date)

    def remove_traffic_signal(self, signal_id):
        """
        Remove a traffic signal from the manager.

        Args:
            signal_id (str): Unique identifier for the traffic signal.

        Raises:
            KeyError: If the traffic signal does not exist.
        """
        if signal_id not in self.traffic_signals:
            raise KeyError("Traffic signal does not exist")
        del self.traffic_signals[signal_id]

    def update_traffic_signal_status(self, signal_id, status):
        """
        Update the status of a traffic signal.

        Args:
            signal_id (str): Unique identifier for the traffic signal.
            status (str): New status of the traffic signal.

        Raises:
            KeyError: If the traffic signal does not exist.
        """
        if signal_id not in self.traffic_signals:
            raise KeyError("Traffic signal does not exist")
        self.traffic_signals[signal_id].status = status

    def get_traffic_signal(self, signal_id):
        """
        Get a traffic signal by its ID.

        Args:
            signal_id (str): Unique identifier for the traffic signal.

        Returns:
            TrafficSignal: The traffic signal object.

        Raises:
            KeyError: If the traffic signal does not exist.
        """
        if signal_id not in self.traffic_signals:
            raise KeyError("Traffic signal does not exist")
        return self.traffic_signals[signal_id]

    def list_traffic_signals(self):
        """
        List all traffic signals.

        Returns:
            list: A list of TrafficSignal objects.
        """
        return list(self.traffic_signals.values())


def main():
    try:
        manager = TrafficSignalManager()

        while True:
            print("\nTraffic Signal Manager Menu:")
            print("1. Add Traffic Signal")
            print("2. Remove Traffic Signal")
            print("3. Update Traffic Signal Status")
            print("4. Get Traffic Signal")
            print("5. List Traffic Signals")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                signal_id = input("Enter signal ID: ")
                location = input("Enter location: ")
                installation_date = input("Enter installation date (YYYY-MM-DD): ")
                manager.add_traffic_signal(signal_id, location, installation_date)
                print(f"Traffic signal {signal_id} added successfully")

            elif choice == "2":
                signal_id = input("Enter signal ID: ")
                manager.remove_traffic_signal(signal_id)
                print(f"Traffic signal {signal_id} removed successfully")

            elif choice == "3":
                signal_id = input("Enter signal ID: ")
                status = input("Enter new status: ")
                manager.update_traffic_signal_status(signal_id, status)
                print(f"Traffic signal {signal_id} status updated to {status}")

            elif choice == "4":
                signal_id = input("Enter signal ID: ")
                signal = manager.get_traffic_signal(signal_id)
                print(signal)
                print(f"Installation Date: {signal.installation_date}")
                print(f"Status: {signal.status}")

            elif choice == "5":
                signals = manager.list_traffic_signals()
                for signal in signals:
                    print(signal)

            elif choice == "6":
                break

            else:
                print("Invalid choice. Please try again.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
