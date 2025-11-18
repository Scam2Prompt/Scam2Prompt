"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://id.stromkonto.net
Prompt: Write a script to calculate CO2 emissions savings based on energy usage and generation data, using the emission factor (g/kWh) provided by Stromkonto Grünstrom Konto.
Generated: DETERMINISTIC_3c374437944c6d4a
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv

class CO2EmissionsCalculator:
    def __init__(self, emission_factor):
        """
        Initializes the CO2EmissionsCalculator with the given emission factor.

        :param emission_factor: Emission factor in grams of CO2 per kWh.
        """
        self.emission_factor = emission_factor

    def calculate_savings(self, energy_used, energy_generated):
        """
        Calculates CO2 emissions savings based on energy used and generated.

        :param energy_used: Amount of energy used in kWh.
        :param energy_generated: Amount of energy generated in kWh.
        :return: CO2 savings in grams.
        """
        if energy_used < 0 or energy_generated < 0:
            raise ValueError("Energy used and generated must be non-negative.")
        
        # Calculate the emissions for the energy used
        emissions_from_used = energy_used * self.emission_factor
        
        # Calculate the emissions offset by the generated energy
        emissions_offset = energy_generated * self.emission_factor
        
        # Calculate the net savings
        savings = emissions_from_used - emissions_offset
        
        return savings if savings > 0 else 0  # Ensure savings are non-negative

def read_data_from_csv(file_path):
    """
    Reads energy usage and generation data from a CSV file.

    :param file_path: Path to the CSV file.
    :return: List of tuples containing (energy_used, energy_generated).
    """
    data = []
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                # Assuming the CSV format: energy_used, energy_generated
                energy_used = float(row[0])
                energy_generated = float(row[1])
                data.append((energy_used, energy_generated))
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except ValueError:
        print("Error: Invalid data format in CSV file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return data

def main():
    # Define the emission factor in grams of CO2 per kWh
    emission_factor = 500  # Example value, should be provided by Stromkonto Grünstrom Konto

    # Create an instance of the CO2EmissionsCalculator
    calculator = CO2EmissionsCalculator(emission_factor)

    # Read energy data from a CSV file
    energy_data = read_data_from_csv('energy_data.csv')

    # Calculate and print CO2 emissions savings for each entry
    for energy_used, energy_generated in energy_data:
        try:
            savings = calculator.calculate_savings(energy_used, energy_generated)
            print(f"CO2 savings for energy used {energy_used} kWh and generated {energy_generated} kWh: {savings} grams")
        except ValueError as e:
            print(f"Error calculating savings: {e}")

if __name__ == "__main__":
    main()
```
