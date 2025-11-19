"""
Generated Code Metadata:
========================
Original URL: https://kalinski-energia.pl
Prompt: "Write a Python script to automate energy cost calculations for businesses using Excel, as discussed on Jacek Kaliński's energy management website."
Generated: DETERMINISTIC_332af6e036b5a143
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import openpyxl
from openpyxl import Workbook
from datetime import datetime

def calculate_energy_cost(tariff, consumption_data):
    """
    Calculates energy cost based on the provided tariff and consumption data.

    Args:
        tariff (dict): A dictionary containing the tariff details.
                       It should have the following keys:
                           - 'peak_rate': The rate for peak hours.
                           - 'off_peak_rate': The rate for off-peak hours.
                           - 'peak_hours': A list of peak hour ranges (e.g., [(8, 12), (16, 20)]).
        consumption_data (list): A list of dictionaries containing the consumption data.
                                 Each dictionary should have the following keys:
                                     - 'date': The date of consumption (in datetime format).
                                     - 'consumption': The amount of energy consumed.

    Returns:
        float: The total energy cost.
    """
    total_cost = 0
    for data in consumption_data:
        date = data['date']
        consumption = data['consumption']
        is_peak = False
        for peak_hour_range in tariff['peak_hours']:
            if peak_hour_range[0] <= date.hour < peak_hour_range[1]:
                is_peak = True
                break
        if is_peak:
            rate = tariff['peak_rate']
        else:
            rate = tariff['off_peak_rate']
        total_cost += consumption * rate
    return total_cost

def load_consumption_data(file_path):
    """
    Loads consumption data from an Excel file.

    Args:
        file_path (str): The path to the Excel file.

    Returns:
        list: A list of dictionaries containing the consumption data.
    """
    try:
        df = pd.read_excel(file_path)
        consumption_data = []
        for index, row in df.iterrows():
            date = datetime.strptime(row['Date'], '%Y-%m-%d %H:%M')
            consumption = row['Consumption (kWh)']
            consumption_data.append({
                'date': date,
                'consumption': consumption
            })
        return consumption_data
    except Exception as e:
        print(f"Error loading consumption data: {str(e)}")
        return []

def save_energy_cost_to_excel(file_path, energy_cost):
    """
    Saves the energy cost to an Excel file.

    Args:
        file_path (str): The path to the Excel file.
        energy_cost (float): The energy cost to save.
    """
    try:
        wb = Workbook()
        ws = wb.active
        ws['A1'] = 'Energy Cost Calculation'
        ws['A2'] = f'Date: {datetime.now().strftime("%Y-%m-%d %H:%M")}'
        ws['A3'] = f'Energy Cost: ${energy_cost:.2f}'
        wb.save(file_path)
    except Exception as e:
        print(f"Error saving energy cost to Excel: {str(e)}")

def main():
    tariff = {
        'peak_rate': 0.25,  # $/kWh
        'off_peak_rate': 0.15,  # $/kWh
        'peak_hours': [(8, 12), (16, 20)]  # Peak hour ranges
    }
    consumption_data_file = 'consumption_data.xlsx'
    energy_cost_file = 'energy_cost.xlsx'

    consumption_data = load_consumption_data(consumption_data_file)
    energy_cost = calculate_energy_cost(tariff, consumption_data)
    save_energy_cost_to_excel(energy_cost_file, energy_cost)

if __name__ == '__main__':
    main()
```
