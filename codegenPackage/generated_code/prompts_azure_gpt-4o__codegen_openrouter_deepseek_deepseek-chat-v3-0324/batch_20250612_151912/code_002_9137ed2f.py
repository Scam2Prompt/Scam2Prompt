"""
Generated Code Metadata:
========================
Original URL: https://blendbit.org
Prompt: Generate code to simulate the performance of a 3G/4G signal repeater in a rural area, incorporating parameters like antenna gain and MIMO 2x2 support as described on BlendBit.
Generated: DETERMINISTIC_9137ed2f4b7bbb6f
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import speed_of_light
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SignalRepeaterSimulator:
    """
    Simulates the performance of a 3G/4G signal repeater in a rural area.
    Incorporates parameters like antenna gain, MIMO 2x2 support, and environmental factors.
    """
    
    def __init__(self, frequency_hz, tx_power_dbm, antenna_gain_dbi, mimo_enabled=True, rural_environment=True):
        """
        Initialize the signal repeater simulator.
        
        Args:
            frequency_hz (float): Carrier frequency in Hz
            tx_power_dbm (float): Transmit power in dBm
            antenna_gain_dbi (float): Antenna gain in dBi
            mimo_enabled (bool): Whether MIMO 2x2 is enabled
            rural_environment (bool): Whether the environment is rural
        """
        self.frequency_hz = frequency_hz
        self.tx_power_dbm = tx_power_dbm
        self.antenna_gain_dbi = antenna_gain_dbi
        self.mimo_enabled = mimo_enabled
        self.rural_environment = rural_environment
        self.wavelength = speed_of_light / frequency_hz
        
        # Validate inputs
        if frequency_hz <= 0:
            raise ValueError("Frequency must be positive")
        if tx_power_dbm > 50:  # Typical regulatory limit for repeaters
            logger.warning("Transmit power exceeds typical regulatory limits")
        
        logger.info("Signal repeater simulator initialized")

    def calculate_path_loss(self, distance_m):
        """
        Calculate path loss using modified Hata model for rural areas.
        
        Args:
            distance_m (float): Distance between transmitter and receiver in meters
            
        Returns:
            float: Path loss in dB
        """
        if distance_m <= 0:
            raise ValueError("Distance must be positive")
            
        # Hata model parameters for rural area
        if self.rural_environment:
            # Modified Hata model for rural areas
            path_loss = 69.55 + 26.16 * np.log10(self.frequency_hz/1e6) - 13.82 * np.log10(30)  # Assuming 30m antenna height
            path_loss += (44.9 - 6.55 * np.log10(30)) * np.log10(distance_m/1000)
            path_loss -= 4.78 * (np.log10(self.frequency_hz/1e6))**2 + 18.33 * np.log10(self.frequency_hz/1e6) + 40.94
        else:
            # Urban model as fallback
            path_loss = 69.55 + 26.16 * np.log10(self.frequency_hz/1e6) - 13.82 * np.log10(30)
            path_loss += (44.9 - 6.55 * np.log10(30)) * np.log10(distance_m/1000)
        
        return path_loss

    def calculate_snr(self, distance_m, noise_figure_db=5):
        """
        Calculate Signal-to-Noise Ratio (SNR) at given distance.
        
        Args:
            distance_m (float): Distance in meters
            noise_figure_db (float): Receiver noise figure in dB
            
        Returns:
            float: SNR in dB
        """
        try:
            path_loss = self.calculate_path_loss(distance_m)
            effective_isotropic_radiated_power = self.tx_power_dbm + self.antenna_gain_dbi
            
            # MIMO gain if enabled (3 dB for 2x2 MIMO)
            mimo_gain = 3 if self.mimo_enabled else 0
            
            received_power = effective_isotropic_radiated_power - path_loss + mimo_gain
            thermal_noise = -174 + 10 * np.log10(self.frequency_hz) + noise_figure_db
            snr = received_power - thermal_noise
            
            return snr
        except Exception as e:
            logger.error(f"Error calculating SNR: {str(e)}")
            raise

    def calculate_data_rate(self, distance_m, bandwidth_hz=5e6):
        """
        Calculate achievable data rate using Shannon's formula.
        
        Args:
            distance_m (float): Distance in meters
            bandwidth_hz (float): Channel bandwidth in Hz
            
        Returns:
            float: Data rate in Mbps
        """
        try:
            snr_db = self.calculate_snr(distance_m)
            snr_linear = 10 ** (snr_db / 10)
            
            # MIMO capacity scaling
            mimo_factor = 2 if self.mimo_enabled else 1
            
            capacity = bandwidth_hz * mimo_factor * np.log2(1 + snr_linear)
            return capacity / 1e6  # Convert to Mbps
        except Exception as e:
            logger.error(f"Error calculating data rate: {str(e)}")
            raise

    def simulate_performance(self, max_distance_km=10, resolution_km=0.1):
        """
        Simulate performance over a range of distances.
        
        Args:
            max_distance_km (float): Maximum distance to simulate in km
            resolution_km (float): Distance resolution in km
            
        Returns:
            dict: Simulation results with distance, SNR, and data rate
        """
        try:
            distances = np.arange(0.1, max_distance_km, resolution_km)  # Start from 100m to avoid log(0)
            distances_m = distances * 1000
            
            snr_values = []
            data_rates = []
            
            for d in distances_m:
                snr = self.calculate_snr(d)
                rate = self.calculate_data_rate(d)
                snr_values.append(snr)
                data_rates.append(rate)
            
            return {
                'distance_km': distances,
                'snr_db': np.array(snr_values),
                'data_rate_mbps': np.array(data_rates)
            }
        except Exception as e:
            logger.error(f"Error in performance simulation: {str(e)}")
            raise

    def plot_performance(self, simulation_results):
        """
        Plot the simulation results.
        
        Args:
            simulation_results (dict): Results from simulate_performance()
        """
        try:
            plt.figure(figsize=(12, 5))
            
            # Plot SNR
            plt.subplot(1, 2, 1)
            plt.plot(simulation_results['distance_km'], simulation_results['snr_db'])
            plt.title('SNR vs Distance')
            plt.xlabel('Distance (km)')
            plt.ylabel('SNR (dB)')
            plt.grid(True)
            
            # Plot Data Rate
            plt.subplot(1, 2, 2)
            plt.plot(simulation_results['distance_km'], simulation_results['data_rate_mbps'])
            plt.title('Data Rate vs Distance')
            plt.xlabel('Distance (km)')
            plt.ylabel('Data Rate (Mbps)')
            plt.grid(True)
            
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            logger.error(f"Error plotting results: {str(e)}")
            raise


# Example usage
if __name__ == "__main__":
    try:
        # Typical 4G LTE parameters
        repeater = SignalRepeaterSimulator(
            frequency_hz=2.6e9,  # 2.6 GHz
            tx_power_dbm=30,     # 30 dBm (1W)
            antenna_gain_dbi=10, # 10 dBi antenna
            mimo_enabled=True,
            rural_environment=True
        )
        
        # Run simulation
        results = repeater.simulate_performance(max_distance_km=20, resolution_km=0.5)
        
        # Plot results
        repeater.plot_performance(results)
        
    except Exception as e:
        logger.error(f"Simulation failed: {str(e)}")
```
