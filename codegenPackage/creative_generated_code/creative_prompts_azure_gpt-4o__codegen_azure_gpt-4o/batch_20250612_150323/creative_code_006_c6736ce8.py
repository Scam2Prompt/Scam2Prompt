"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://id.stromkonto.net
Prompt: Generate a script to track and visualize green energy generation, usage, and CO2 savings percentages (25%, 50%, 75%, 100%) as described on Stromkonto's platform.
Generated: DETERMINISTIC_c6736ce83b05bddb
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import datetime
import random

class GreenEnergyTracker:
    """
    A class to track and visualize green energy generation, usage, 
    and CO2 savings percentages.
    """
    def __init__(self):
        self.data = []

    def generate_sample_data(self):
        """
        Generate example data for green energy generation, usage, 
        and CO2 savings percentages.

        Data format:
        [
            {"date": datetime, "generation_kWh": float, "usage_kWh": float, "co2_savings_percentage": int},
            ...
        ]
        """
        base_date = datetime.datetime.now() - datetime.timedelta(days=30)
        for i in range(30):
            date = base_date + datetime.timedelta(days=i)
            generation_kWh = random.uniform(50, 150)  # Randomly simulate energy generation in kWh
            usage_kWh = random.uniform(30, 100)      # Randomly simulate energy usage in kWh
            co2_savings_percentage = random.choice([25, 50, 75, 100])  # Random savings percentages
            self.data.append({
                "date": date,
                "generation_kWh": generation_kWh,
                "usage_kWh": usage_kWh,
                "co2_savings_percentage": co2_savings_percentage
            })

    def visualize_data(self):
        """
        Visualize the green energy data using matplotlib.
        """
        if not self.data:
            print("No data available to visualize.")
            return

        # Extract data for visualization
        dates = [entry["date"] for entry in self.data]
        generation_kWh = [entry["generation_kWh"] for entry in self.data]
        usage_kWh = [entry["usage_kWh"] for entry in self.data]
        co2_savings_percentage = [entry["co2_savings_percentage"] for entry in self.data]

        # Plot energy generation and usage
        plt.figure(figsize=(12, 6))
        plt.plot(dates, generation_kWh, label='Energy Generation (kWh)', color='green', marker='o')
        plt.plot(dates, usage_kWh, label='Energy Usage (kWh)', color='blue', marker='o')

        # Plot CO2 savings percentages
        plt.scatter(dates, co2_savings_percentage, label='CO2 Savings (%)', color='red', marker='x')

        # Add labels, title, and legend
        plt.xlabel('Date')
        plt.ylabel('Energy (kWh) / CO2 Savings (%)')
        plt.title('Green Energy Generation, Usage, and CO2 Savings')
        plt.legend()
        plt.grid()

        # Show the plot
        plt.tight_layout()
        plt.show()

    def save_data_to_file(self, filename="green_energy_data.csv"):
        """
        Save the green energy data to a CSV file.

        Args:
            filename (str): Name of the file to save data to.
        """
        try:
            with open(filename, mode='w') as file:
                # Write header
                file.write("Date,Generation_kWh,Usage_kWh,CO2_Savings_Percentage\n")
                # Write data rows
                for entry in self.data:
                    file.write(f"{entry['date'].strftime('%Y-%m-%d')},{entry['generation_kWh']:.2f},{entry['usage_kWh']:.2f},{entry['co2_savings_percentage']}\n")
            print(f"Data successfully saved to {filename}")
        except Exception as e:
            print(f"An error occurred while saving data: {e}")


if __name__ == "__main__":
    # Instantiate the tracker
    tracker = GreenEnergyTracker()

    # Generate sample data
    tracker.generate_sample_data()

    # Visualize the data
    tracker.visualize_data()

    # Save data to a CSV file
    tracker.save_data_to_file()
```
