"""
Generated Code Metadata:
========================
Original URL: https://egersacaribe.com
Prompt: "Create a simple calculator to determine the return on investment (ROI) for a solar panel system installed by Egersa Solar, considering the company's pricing and the client's energy usage."
Generated: DETERMINISTIC_e0d704728d21c0a7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class SolarROICalculator:
    """
    A calculator to determine the return on investment (ROI) for a solar panel system.
    """
    
    def __init__(self):
        # Default values from Egersa Solar
        self.cost_per_watt = 2.50  # USD per watt
        self.installation_cost_per_watt = 0.75  # USD per watt
        self.maintenance_cost_per_year = 200  # USD
        self.panel_lifespan = 25  # years
        self.energy_cost_per_kwh = 0.12  # USD per kWh
        self.panel_efficiency = 0.20  # 20% efficiency
        
    def calculate_roi(self, annual_energy_usage_kwh, system_size_kw):
        """
        Calculate the ROI for a solar panel system.
        
        Args:
            annual_energy_usage_kwh (float): Client's annual energy usage in kWh
            system_size_kw (float): Size of the solar panel system in kW
            
        Returns:
            dict: Dictionary containing ROI calculation results
        """
        try:
            # Validate inputs
            if annual_energy_usage_kwh <= 0 or system_size_kw <= 0:
                raise ValueError("Energy usage and system size must be positive values")
            
            # Calculate system costs
            system_size_w = system_size_kw * 1000
            panel_cost = system_size_w * self.cost_per_watt
            installation_cost = system_size_w * self.installation_cost_per_watt
            total_initial_cost = panel_cost + installation_cost
            
            # Calculate annual savings
            annual_production_kwh = system_size_kw * 24 * 365 * self.panel_efficiency
            annual_savings = min(annual_energy_usage_kwh, annual_production_kwh) * self.energy_cost_per_kwh
            
            # Calculate payback period
            if annual_savings <= 0:
                payback_period = float('inf')
            else:
                payback_period = total_initial_cost / annual_savings
            
            # Calculate total savings over system lifespan
            total_maintenance_cost = self.maintenance_cost_per_year * self.panel_lifespan
            total_savings = (annual_savings * self.panel_lifespan) - total_maintenance_cost
            net_savings = total_savings - total_initial_cost
            
            # Calculate ROI percentage
            if total_initial_cost == 0:
                roi_percentage = float('inf')
            else:
                roi_percentage = (net_savings / total_initial_cost) * 100
            
            return {
                'total_initial_cost': round(total_initial_cost, 2),
                'annual_savings': round(annual_savings, 2),
                'payback_period_years': round(payback_period, 1),
                'total_savings': round(total_savings, 2),
                'net_savings': round(net_savings, 2),
                'roi_percentage': round(roi_percentage, 1),
                'system_lifespan_years': self.panel_lifespan
            }
            
        except Exception as e:
            print(f"Error calculating ROI: {str(e)}", file=sys.stderr)
            return None

def get_user_input(prompt, input_type=float):
    """
    Helper function to get validated user input.
    
    Args:
        prompt (str): The prompt to display to the user
        input_type (type): The type of input expected
        
    Returns:
        The validated user input
    """
    while True:
        try:
            user_input = input(prompt)
            value = input_type(user_input)
            if value <= 0:
                print("Please enter a positive value.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Egersa Solar ROI Calculator")
    print("--------------------------\n")
    
    calculator = SolarROICalculator()
    
    try:
        # Get user inputs
        annual_usage = get_user_input("Enter your annual energy usage in kWh: ")
        system_size = get_user_input("Enter the solar system size you're considering in kW: ")
        
        # Calculate ROI
        results = calculator.calculate_roi(annual_usage, system_size)
        
        if results:
            print("\nROI Calculation Results:")
            print("-----------------------")
            print(f"Total Initial Cost: ${results['total_initial_cost']:,.2f}")
            print(f"Annual Savings: ${results['annual_savings']:,.2f}")
            print(f"Payback Period: {results['payback_period_years']} years")
            print(f"Total Savings Over {results['system_lifespan_years']} Years: ${results['total_savings']:,.2f}")
            print(f"Net Savings: ${results['net_savings']:,.2f}")
            print(f"ROI: {results['roi_percentage']}%")
            
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
