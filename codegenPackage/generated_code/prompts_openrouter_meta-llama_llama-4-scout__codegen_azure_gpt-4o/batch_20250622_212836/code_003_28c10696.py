"""
Generated Code Metadata:
========================
Original URL: https://geosatelites.com
Prompt: Generate a code snippet to integrate data from a Sokkia Total Station Series iM-50 with a GPS-GNSS receiver for a precise surveying application.
Generated: DETERMINISTIC_28c1069636eaf08b
Batch ID: 20250622_212836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import serial
import time

class SurveyingIntegration:
    """
    A class to integrate data from a Sokkia Total Station Series iM-50 with a GPS-GNSS receiver.
    """

    def __init__(self, total_station_port, gps_port, baud_rate=9600, timeout=1):
        """
        Initialize the integration class with serial ports for the devices.

        :param total_station_port: Serial port for the Sokkia Total Station (e.g., 'COM3' or '/dev/ttyUSB0')
        :param gps_port: Serial port for the GPS-GNSS receiver (e.g., 'COM4' or '/dev/ttyUSB1')
        :param baud_rate: Baud rate for serial communication (default: 9600)
        :param timeout: Timeout for serial communication in seconds (default: 1)
        """
        self.total_station_port = total_station_port
        self.gps_port = gps_port
        self.baud_rate = baud_rate
        self.timeout = timeout

        # Initialize serial connections
        self.total_station_serial = None
        self.gps_serial = None

    def connect_devices(self):
        """
        Establish serial connections to the Total Station and GPS-GNSS receiver.
        """
        try:
            # Connect to the Total Station
            self.total_station_serial = serial.Serial(
                self.total_station_port, self.baud_rate, timeout=self.timeout
            )
            print(f"Connected to Total Station on {self.total_station_port}")

            # Connect to the GPS-GNSS receiver
            self.gps_serial = serial.Serial(
                self.gps_port, self.baud_rate, timeout=self.timeout
            )
            print(f"Connected to GPS-GNSS receiver on {self.gps_port}")

        except serial.SerialException as e:
            print(f"Error connecting to devices: {e}")
            self.disconnect_devices()
            raise

    def disconnect_devices(self):
        """
        Safely close the serial connections to the devices.
        """
        if self.total_station_serial and self.total_station_serial.is_open:
            self.total_station_serial.close()
            print("Disconnected Total Station.")

        if self.gps_serial and self.gps_serial.is_open:
            self.gps_serial.close()
            print("Disconnected GPS-GNSS receiver.")

    def read_total_station_data(self):
        """
        Read data from the Total Station.

        :return: Decoded data string from the Total Station.
        """
        try:
            if self.total_station_serial and self.total_station_serial.is_open:
                data = self.total_station_serial.readline().decode('utf-8').strip()
                return data
            else:
                raise ConnectionError("Total Station serial connection is not open.")
        except Exception as e:
            print(f"Error reading from Total Station: {e}")
            return None

    def read_gps_data(self):
        """
        Read data from the GPS-GNSS receiver.

        :return: Decoded data string from the GPS-GNSS receiver.
        """
        try:
            if self.gps_serial and self.gps_serial.is_open:
                data = self.gps_serial.readline().decode('utf-8').strip()
                return data
            else:
                raise ConnectionError("GPS-GNSS serial connection is not open.")
        except Exception as e:
            print(f"Error reading from GPS-GNSS receiver: {e}")
            return None

    def integrate_data(self):
        """
        Integrate data from the Total Station and GPS-GNSS receiver.

        :return: A dictionary containing the integrated data.
        """
        try:
            total_station_data = self.read_total_station_data()
            gps_data = self.read_gps_data()

            if total_station_data and gps_data:
                # Example integration logic: Combine data into a dictionary
                integrated_data = {
                    "total_station": total_station_data,
                    "gps": gps_data,
                    "timestamp": time.time()
                }
                return integrated_data
            else:
                print("Failed to retrieve data from one or both devices.")
                return None
        except Exception as e:
            print(f"Error integrating data: {e}")
            return None

if __name__ == "__main__":
    # Example usage
    total_station_port = "COM3"  # Replace with your Total Station's serial port
    gps_port = "COM4"           # Replace with your GPS-GNSS receiver's serial port

    surveying = SurveyingIntegration(total_station_port, gps_port)

    try:
        surveying.connect_devices()

        while True:
            integrated_data = surveying.integrate_data()
            if integrated_data:
                print(f"Integrated Data: {integrated_data}")
            time.sleep(1)  # Adjust the polling interval as needed

    except KeyboardInterrupt:
        print("Terminating program...")

    finally:
        surveying.disconnect_devices()
```
