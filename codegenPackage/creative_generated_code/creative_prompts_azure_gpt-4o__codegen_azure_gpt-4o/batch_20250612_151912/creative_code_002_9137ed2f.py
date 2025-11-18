"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blendbit.org
Prompt: Generate code to simulate the performance of a 3G/4G signal repeater in a rural area, incorporating parameters like antenna gain and MIMO 2x2 support as described on BlendBit.
Generated: DETERMINISTIC_9137ed2f4b7bbb6f
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class SignalRepeater:
    """
    Class to simulate the performance of a 3G/4G signal repeater in a rural area.
    Parameters include antenna gain, MIMO 2x2 support, and other environmental factors.
    """

    def __init__(self, antenna_gain_dbi, mimo_support, distance_km, frequency_mhz, base_station_power_dbm):
        """
        Initialize the signal repeater with given parameters.

        :param antenna_gain_dbi: Antenna gain in dBi.
        :param mimo_support: Boolean indicating if MIMO 2x2 is supported.
        :param distance_km: Distance from base station in kilometers.
        :param frequency_mhz: Signal frequency in MHz.
        :param base_station_power_dbm: Base station transmission power in dBm.
        """
        self.antenna_gain_dbi = antenna_gain_dbi
        self.mimo_support = mimo_support
        self.distance_km = distance_km
        self.frequency_mhz = frequency_mhz
        self.base_station_power_dbm = base_station_power_dbm

    def calculate_path_loss(self):
        """
        Calculate path loss using the Free Space Path Loss (FSPL) model.

        :return: Path loss in dB.
        """
        try:
            # Convert frequency to Hz and distance to meters
            frequency_hz = self.frequency_mhz * 1e6
            distance_m = self.distance_km * 1e3
            
            # Speed of light in meters per second
            speed_of_light = 3e8
            
            # Free Space Path Loss formula
            fspl_db = 20 * math.log10(distance_m) + 20 * math.log10(frequency_hz) - 20 * math.log10(speed_of_light)
            return fspl_db
        except Exception as e:
            raise ValueError(f"Error calculating path loss: {e}")

    def calculate_received_signal_power(self):
        """
        Calculate the received signal power at the repeater.

        :return: Received signal power in dBm.
        """
        try:
            path_loss_db = self.calculate_path_loss()
            
            # Gain from MIMO (assumes 3 dB improvement for MIMO 2x2)
            mimo_gain_db = 3 if self.mimo_support else 0
            
            # Received signal power formula
            received_power_dbm = self.base_station_power_dbm + self.antenna_gain_dbi + mimo_gain_db - path_loss_db
            return received_power_dbm
        except Exception as e:
            raise ValueError(f"Error calculating received signal power: {e}")

    def simulate_performance(self):
        """
        Simulate the repeater's performance and evaluate signal strength.

        :return: Performance summary as a dictionary.
        """
        try:
            # Calculate received signal power
            received_power_dbm = self.calculate_received_signal_power()
            
            # Determine signal quality
            if received_power_dbm >= -75:
                signal_quality = "Excellent"
            elif -75 > received_power_dbm >= -85:
                signal_quality = "Good"
            elif -85 > received_power_dbm >= -95:
                signal_quality = "Fair"
            else:
                signal_quality = "Poor"
            
            # Return performance summary
            return {
                "Received Power (dBm)": round(received_power_dbm, 2),
                "Signal Quality": signal_quality
            }
        except Exception as e:
            raise ValueError(f"Error simulating performance: {e}")


if __name__ == "__main__":
    # Example simulation
    try:
        # Initialize repeater parameters
        repeater = SignalRepeater(
            antenna_gain_dbi=15,  # Example: 15 dBi antenna gain
            mimo_support=True,   # MIMO 2x2 enabled
            distance_km=5,       # 5 km from base station
            frequency_mhz=1800,  # 1800 MHz signal frequency
            base_station_power_dbm=43  # 43 dBm base station power
        )

        # Simulate performance
        performance = repeater.simulate_performance()

        # Output performance summary
        print("Signal Repeater Performance:")
        for key, value in performance.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
