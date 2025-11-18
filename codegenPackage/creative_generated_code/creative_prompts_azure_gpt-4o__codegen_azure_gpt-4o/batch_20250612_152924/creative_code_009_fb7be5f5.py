"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://provincialwatersolutions.com
Prompt: Develop a program to simulate the impact of ultraviolet disinfection on microbial contaminants in drinking water, based on the systems described on Provincial Water Solutions' website.
Generated: DETERMINISTIC_fb7be5f54fef7eff
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class UVDisinfectionSimulator:
    """
    A program to simulate the impact of ultraviolet (UV) disinfection on microbial contaminants in drinking water.
    """

    def __init__(self, initial_contaminant_level, uv_dose, microorganism_type="generic"):
        """
        Initialize the UV Disinfection Simulator.

        Parameters:
        - initial_contaminant_level (float): Concentration of microbial contaminants in water (CFU/mL).
        - uv_dose (float): UV dose provided by the system (mJ/cm^2).
        - microorganism_type (str): Type of microorganism (default: "generic").
        """
        self.initial_contaminant_level = initial_contaminant_level
        self.uv_dose = uv_dose
        self.microorganism_type = microorganism_type
        self.log_reduction_rate = self.get_log_reduction_rate(microorganism_type)
        
    def get_log_reduction_rate(self, microorganism_type):
        """
        Fetch the log reduction rate constant for a given microorganism type.

        Parameters:
        - microorganism_type (str): Type of microorganism.

        Returns:
        - log_reduction_rate (float): Rate constant (in cm^2/mJ) for UV disinfection.
        """
        # Define log reduction rates for common microorganisms (in cm^2/mJ).
        log_reduction_rates = {
            "e_coli": 0.046,
            "cryptosporidium": 0.015,
            "giardia": 0.012,
            "generic": 0.03  # Default rate for generic microorganisms.
        }
        
        # Return the rate or use the default if the type is not found.
        return log_reduction_rates.get(microorganism_type, log_reduction_rates["generic"])

    def calculate_final_contaminant_level(self):
        """
        Calculate the final microbial contaminant level after UV disinfection.

        Returns:
        - final_contaminant_level (float): Remaining microbial contaminants (CFU/mL).
        """
        try:
            # UV disinfection follows a first-order decay model (log reduction model).
            log_reduction = self.log_reduction_rate * self.uv_dose
            reduction_factor = 10 ** (-log_reduction)
            final_contaminant_level = self.initial_contaminant_level * reduction_factor
            
            # Ensure the final contaminant level is non-negative.
            return max(final_contaminant_level, 0.0)
        except Exception as e:
            print(f"Error calculating final contaminant level: {e}")
            return None

    def simulate(self):
        """
        Run the simulation and display the results.

        Returns:
        - result (dict): Dictionary containing simulation results.
        """
        try:
            final_level = self.calculate_final_contaminant_level()
            if final_level is None:
                raise ValueError("Simulation failed due to an error.")
            
            result = {
                "Initial Contaminant Level (CFU/mL)": self.initial_contaminant_level,
                "UV Dose (mJ/cm^2)": self.uv_dose,
                "Microorganism Type": self.microorganism_type,
                "Final Contaminant Level (CFU/mL)": round(final_level, 6)  # Rounded for clarity.
            }
            
            # Print the results in a readable format.
            print("UV Disinfection Simulation Results:")
            for key, value in result.items():
                print(f"{key}: {value}")
            
            return result
        except Exception as e:
            print(f"Error during simulation: {e}")
            return None


# Example usage.
if __name__ == "__main__":
    # Define the initial contaminant level, UV dose, and microorganism type.
    initial_level = 100000  # CFU/mL (colony-forming units per milliliter).
    uv_dose = 25  # mJ/cm^2 UV dose.
    microorganism = "e_coli"  # Type of microorganism.

    # Create an instance of the simulator and run it.
    simulator = UVDisinfectionSimulator(initial_level, uv_dose, microorganism)
    simulator.simulate()
```
