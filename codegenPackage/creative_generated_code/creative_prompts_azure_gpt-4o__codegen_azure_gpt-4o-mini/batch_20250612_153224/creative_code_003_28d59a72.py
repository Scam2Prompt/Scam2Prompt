"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vinaroy.com.vn
Prompt: Create a program to compare the performance metrics (e.g., airflow rate, noise level) of different VinaRoy air blower models, such as FB150 and FB250.
Generated: DETERMINISTIC_28d59a72deace617
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt

class AirBlower:
    """
    Class to represent an air blower with performance metrics.
    Attributes:
        model (str): The model of the air blower.
        airflow_rate (float): The airflow rate in cubic feet per minute (CFM).
        noise_level (float): The noise level in decibels (dB).
    """
    def __init__(self, model: str, airflow_rate: float, noise_level: float):
        """
        Initializes an AirBlower instance.

        Parameters:
            model (str): The model of the air blower.
            airflow_rate (float): The airflow rate in CFM.
            noise_level (float): The noise level in dB.
        """
        self.model = model
        self.airflow_rate = airflow_rate
        self.noise_level = noise_level

    def __repr__(self):
        return f"{self.model}: Airflow Rate={self.airflow_rate} CFM, Noise Level={self.noise_level} dB"

def compare_blower_performance(blowers):
    """
    Compares the performance of different air blower models and visualizes the metrics.

    Parameters:
        blowers (list): A list of AirBlower instances to compare.
    """
    # Creating a DataFrame for better visualization and manipulation
    blower_data = {
        'Model': [blower.model for blower in blowers],
        'Airflow Rate (CFM)': [blower.airflow_rate for blower in blowers],
        'Noise Level (dB)': [blower.noise_level for blower in blowers]
    }
    
    df = pd.DataFrame(blower_data)

    try:
        # Plotting Airflow Rate
        plt.figure(figsize=(10, 5))
        plt.bar(df['Model'], df['Airflow Rate (CFM)'], color='blue', alpha=0.6, label='Airflow Rate (CFM)')
        plt.xlabel('Blower Model')
        plt.ylabel('Airflow Rate (CFM)')
        plt.title('Airflow Rate Comparison of VinaRoy Air Blowers')
        plt.grid(axis='y')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # Plotting Noise Level
        plt.figure(figsize=(10, 5))
        plt.bar(df['Model'], df['Noise Level (dB)'], color='red', alpha=0.6, label='Noise Level (dB)')
        plt.xlabel('Blower Model')
        plt.ylabel('Noise Level (dB)')
        plt.title('Noise Level Comparison of VinaRoy Air Blowers')
        plt.grid(axis='y')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occurred while plotting the data: {e}")

if __name__ == "__main__":
    # Creating instances of air blowers
    fb150 = AirBlower(model='FB150', airflow_rate=150, noise_level=60)
    fb250 = AirBlower(model='FB250', airflow_rate=250, noise_level=65)

    # Collecting blower models in a list
    blowers = [fb150, fb250]

    # Comparing performance metrics
    compare_blower_performance(blowers)
```
