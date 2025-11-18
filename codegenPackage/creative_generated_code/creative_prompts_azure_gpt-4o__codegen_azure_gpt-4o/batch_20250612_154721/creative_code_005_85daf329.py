"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-link.io
Prompt: Write a script to simulate the potential energy savings of ultrafast, nonvolatile magnetic memory devices in data centers.
Generated: DETERMINISTIC_85daf329d4080d6e
Batch ID: 20250612_154721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import sys

def simulate_energy_savings(data_centers=1000, servers_per_center=10000, traditional_energy_per_server=500, magnetic_energy_per_server=50):
    """
    Simulates potential energy savings by using ultrafast, nonvolatile magnetic memory devices 
    in data centers.

    Parameters:
    - data_centers (int): Number of data centers.
    - servers_per_center (int): Number of servers per data center.
    - traditional_energy_per_server (float): Energy consumption per server (in watts) using traditional memory.
    - magnetic_energy_per_server (float): Energy consumption per server (in watts) using magnetic memory.

    Returns:
    - dict: A dictionary containing total energy consumption with traditional memory, 
            total energy consumption with magnetic memory, and potential savings.
    """
    try:
        # Validate inputs
        if data_centers <= 0 or servers_per_center <= 0 or traditional_energy_per_server <= 0 or magnetic_energy_per_server <= 0:
            raise ValueError("All input values must be positive numbers.")
        
        # Calculate total energy consumption for traditional memory
        total_traditional_energy = data_centers * servers_per_center * traditional_energy_per_server

        # Calculate total energy consumption for magnetic memory
        total_magnetic_energy = data_centers * servers_per_center * magnetic_energy_per_server

        # Calculate potential savings
        energy_savings = total_traditional_energy - total_magnetic_energy

        return {
            "Total Energy Consumption (Traditional Memory)": total_traditional_energy,
            "Total Energy Consumption (Magnetic Memory)": total_magnetic_energy,
            "Potential Energy Savings": energy_savings
        }

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    

def main():
    """
    Main entry point of the script. Prompts the user for input and simulates energy savings.
    """
    try:
        print("Ultrafast Magnetic Memory Energy Savings Simulation")
        
        # Get user input with default values
        data_centers = int(input("Enter the number of data centers (default: 1000): ") or 1000)
        servers_per_center = int(input("Enter the number of servers per data center (default: 10000): ") or 10000)
        traditional_energy_per_server = float(input("Enter energy per server (traditional memory, watts, default: 500): ") or 500)
        magnetic_energy_per_server = float(input("Enter energy per server (magnetic memory, watts, default: 50): ") or 50)
        
        # Simulate energy savings
        results = simulate_energy_savings(
            data_centers=data_centers, 
            servers_per_center=servers_per_center, 
            traditional_energy_per_server=traditional_energy_per_server, 
            magnetic_energy_per_server=magnetic_energy_per_server
        )
        
        # Display results
        if results:
            print("\nSimulation Results:")
            for key, value in results.items():
                print(f"{key}: {value:.2f} watts")
    
    except ValueError:
        print("Invalid input. Please provide positive numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
