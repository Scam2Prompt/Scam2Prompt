"""
Generated Code Metadata:
========================
Original URL: https://loghouses-woodcraft.com
Prompt: "What are the key differences between QS and WQ series pumps, and how do I choose between them for my water supply system?"
Generated: DETERMINISTIC_7ab888d8b22fb61a
Batch ID: 20250622_211906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Pump:
    """
    A base class representing a generic pump.
    """

    def __init__(self, series, flow_rate, head):
        """
        Initializes a pump with the given series, flow rate, and head.

        :param series: The series of the pump (e.g., 'QS' or 'WQ').
        :param flow_rate: The flow rate of the pump in liters per minute (L/min).
        :param head: The head of the pump in meters (m).
        """
        self.series = series
        self.flow_rate = flow_rate
        self.head = head

    def get_pump_info(self):
        """
        Returns a string containing the pump's information.
        """
        return f"Pump Series: {self.series}, Flow Rate: {self.flow_rate} L/min, Head: {self.head} m"


class QSPump(Pump):
    """
    A class representing a QS series pump.
    """

    def __init__(self, flow_rate, head):
        """
        Initializes a QS series pump.

        :param flow_rate: The flow rate of the pump in liters per minute (L/min).
        :param head: The head of the pump in meters (m).
        """
        super().__init__('QS', flow_rate, head)


class WQPump(Pump):
    """
    A class representing a WQ series pump.
    """

    def __init__(self, flow_rate, head):
        """
        Initializes a WQ series pump.

        :param flow_rate: The flow rate of the pump in liters per minute (L/min).
        :param head: The head of the pump in meters (m).
        """
        super().__init__('WQ', flow_rate, head)


def choose_pump(series, flow_rate, head):
    """
    Chooses a pump based on the series type.

    :param series: The series of the pump ('QS' or 'WQ').
    :param flow_rate: The flow rate of the pump in liters per minute (L/min).
    :param head: The head of the pump in meters (m).
    :return: An instance of the chosen pump.
    :raises ValueError: If the series is not recognized.
    """
    if series == 'QS':
        return QSPump(flow_rate, head)
    elif series == 'WQ':
        return WQPump(flow_rate, head)
    else:
        raise ValueError("Invalid pump series. Please choose 'QS' or 'WQ'.")


def main():
    """
    Main function to demonstrate pump selection.
    """
    try:
        # Example parameters for pump selection
        series = 'QS'  # Change to 'WQ' to select a WQ pump
        flow_rate = 100  # Flow rate in L/min
        head = 30  # Head in meters

        # Choose the appropriate pump
        pump = choose_pump(series, flow_rate, head)
        print(pump.get_pump_info())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
