"""
Generated Code Metadata:
========================
Original URL: https://vinaroy.com.vn
Prompt: Create a program to compare the performance metrics (e.g., airflow rate, noise level) of different VinaRoy air blower models, such as FB150 and FB250.
Generated: DETERMINISTIC_28d59a72deace617
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt

class AirBlower:
    """
    A class to represent an air blower model with its performance metrics.
    """

    def __init__(self, model_name, airflow_rate, noise_level):
        """
        Initializes an AirBlower instance.

        :param model_name: str, the name of the air blower model
        :param airflow_rate: float, the airflow rate in cubic feet per minute (CFM)
        :param noise_level: float, the noise level in decibels (dB)
        """
        self.model_name = model_name
        self.airflow_rate = airflow_rate
        self.noise_level = noise_level

    def __repr__(self):
        return f"{self.model_name}: Airflow Rate = {self.airflow_rate} CFM, Noise Level = {self.noise_level} dB"


def compare_blowers(blower_list):
    """
    Compares the performance metrics of different air blower models.

    :param blower_list: list of AirBlower instances
    """
    if not blower_list:
        raise ValueError("The blower list cannot be empty.")

    # Create a DataFrame for better visualization
    data = {
        'Model': [blower.model_name for blower in blower_list],
        'Airflow Rate (CFM)': [blower.airflow_rate for blower in blower_list],
        'Noise Level (dB)': [blower.noise_level for blower in blower_list]
    }
    
    df = pd.DataFrame(data)

    # Display the DataFrame
    print(df)

    # Plotting the performance metrics
    fig, ax1 = plt.subplots()

    # Plot airflow rate
    ax1.set_xlabel('Model')
    ax1.set_ylabel('Airflow Rate (CFM)', color='tab:blue')
    ax1.bar(df['Model'], df['Airflow Rate (CFM)'], color='tab:blue', alpha=0.6, label='Airflow Rate')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    # Create a second y-axis for noise level
    ax2 = ax1.twinx()
    ax2.set_ylabel('Noise Level (dB)', color='tab:red')
    ax2.plot(df['Model'], df['Noise Level (dB)'], color='tab:red', marker='o', label='Noise Level')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    # Title and layout adjustments
    plt.title('Performance Comparison of VinaRoy Air Blower Models')
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    try:
        # Define the air blower models with their performance metrics
        blower_models = [
            AirBlower("FB150", airflow_rate=150, noise_level=70),
            AirBlower("FB250", airflow_rate=250, noise_level=75)
        ]

        # Compare the performance of the defined models
        compare_blowers(blower_models)

    except Exception as e:
        print(f"An error occurred: {e}")
```
