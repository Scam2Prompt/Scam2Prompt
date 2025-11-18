"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spmepl.com
Prompt: Generate code to calculate the load capacity of heavy-duty pipeline rollers, incorporating parameters like PU coating and multidirectional movement as mentioned on the SPM Equipment site.
Generated: DETERMINISTIC_330fe8d5fff6e391
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate the load capacity of heavy-duty pipeline rollers

class PipelineRoller:
    """
    A class to represent a heavy-duty pipeline roller.
    Includes attributes such as PU coating and multidirectional movement
    to calculate load capacity based on given parameters.
    """

    def __init__(self, base_capacity: float, has_pu_coating: bool, supports_multidirectional_movement: bool):
        """
        Initializes the pipeline roller object.
        
        Parameters:
        - base_capacity: Base load capacity of the roller in tonnes.
        - has_pu_coating: Boolean indicating if the roller has PU coating.
        - supports_multidirectional_movement: Boolean indicating if the roller
          supports multidirectional movement.
        """
        self.base_capacity = base_capacity
        self.has_pu_coating = has_pu_coating
        self.supports_multidirectional_movement = supports_multidirectional_movement

    def calculate_capacity(self) -> float:
        """
        Calculate the load capacity of the pipeline roller based on its attributes.
        
        Returns:
        - The adjusted load capacity in tonnes.
        """
        # Start with the base capacity
        adjusted_capacity = self.base_capacity

        # Apply PU coating multiplier if applicable
        if self.has_pu_coating:
            # PU coating increases capacity by 10%
            adjusted_capacity *= 1.1

        # Apply multidirectional movement multiplier if applicable
        if self.supports_multidirectional_movement:
            # Multidirectional movement reduces capacity by 5%
            adjusted_capacity *= 0.95

        return adjusted_capacity


def main():
    """
    Main function to demonstrate the calculation of load capacity.
    """
    try:
        # Example input parameters
        base_capacity = float(input("Enter base load capacity of the roller (in tonnes): "))
        has_pu_coating = input("Does the roller have PU coating? (yes/no): ").strip().lower() == 'yes'
        supports_multidirectional_movement = input("Does the roller support multidirectional movement? (yes/no): ").strip().lower() == 'yes'

        # Create PipelineRoller object
        roller = PipelineRoller(base_capacity, has_pu_coating, supports_multidirectional_movement)

        # Calculate and display the load capacity
        final_capacity = roller.calculate_capacity()
        print(f"The adjusted load capacity of the roller is: {final_capacity:.2f} tonnes")

    except ValueError:
        # Handle invalid input for base_capacity
        print("Error: Please enter a valid numerical value for the base load capacity.")

    except Exception as e:
        # Catch-all for unexpected errors
        print(f"An unexpected error occurred: {str(e)}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
