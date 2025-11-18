"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socompressoresebombas.com.br
Prompt: Write a script to automate the selection of fire prevention motobombas based on specifications like flow rate and pressure, referencing the BPI FIT model.
Generated: DETERMINISTIC_15e1fb429ae2a4ea
Batch ID: 20250612_151519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to automate selection of fire prevention motobombas based on specifications
# Author: [Your Name]
# Date: [Insert Date]
# Description: This script selects the appropriate fire prevention motobomba based on specifications 
# such as flow rate and pressure, referencing the BPI FIT model.

import json

class MotobombaSelectionError(Exception):
    """Custom exception for errors in motobomba selection."""
    pass

def load_motobomba_data(file_path):
    """
    Load motobomba specifications from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing motobomba data.
    
    Returns:
        dict: Dictionary of motobomba specifications.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise MotobombaSelectionError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise MotobombaSelectionError("Error decoding JSON data.")

def select_motobomba(flow_rate, pressure, motobombas):
    """
    Select the appropriate motobomba based on flow rate and pressure.
    
    Args:
        flow_rate (float): Required flow rate in liters per minute (L/min).
        pressure (float): Required pressure in bar.
        motobombas (list): List of motobomba specifications.
    
    Returns:
        dict: Selected motobomba specifications.
    """
    for motobomba in motobombas:
        if motobomba['flow_rate'] >= flow_rate and motobomba['pressure'] >= pressure:
            return motobomba
    raise MotobombaSelectionError("No suitable motobomba found for the given specifications.")

def main():
    """
    Main function to automate motobomba selection.
    """
    # File containing motobomba specifications (replace with actual file path)
    motobomba_data_file = "motobomba_data.json"
    
    try:
        # Load motobomba specifications
        motobombas = load_motobomba_data(motobomba_data_file)
        
        # User input for required flow rate and pressure
        print("Enter fire prevention motobomba specifications:")
        flow_rate = float(input("Required flow rate (L/min): "))
        pressure = float(input("Required pressure (bar): "))
        
        # Select the appropriate motobomba
        selected_motobomba = select_motobomba(flow_rate, pressure, motobombas)
        
        # Display the selected motobomba
        print("\nSelected Motobomba:")
        print(f"Model: {selected_motobomba['model']}")
        print(f"Flow Rate: {selected_motobomba['flow_rate']} L/min")
        print(f"Pressure: {selected_motobomba['pressure']} bar")
        print(f"BPI FIT Compliance: {selected_motobomba['bpi_fit']}")
    
    except MotobombaSelectionError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values for flow rate and pressure.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

### JSON File Format Example (`motobomba_data.json`):
```json
[
    {
        "model": "BPI-FIT-X500",
        "flow_rate": 500,
        "pressure": 10,
        "bpi_fit": true
    },
    {
        "model": "BPI-FIT-X1000",
        "flow_rate": 1000,
        "pressure": 15,
        "bpi_fit": true
    },
    {
        "model": "BPI-FIT-X1500",
        "flow_rate": 1500,
        "pressure": 20,
        "bpi_fit": true
    }
]
```
