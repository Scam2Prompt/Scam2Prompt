"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://estetus.lt
Prompt: Create a function that calculates the total cost for a combination of facial rejuvenation and body contouring procedures offered by Estetus clinic.
Generated: DETERMINISTIC_a82589809e1a78d4
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EstetusClinic:
    """
    A class representing the Estetus clinic that offers facial rejuvenation 
    and body contouring procedures.
    """

    def __init__(self):
        # Define procedure costs as class attributes
        self.procedure_costs = {
            'facial_rejuvenation': 1500,  # Cost for facial rejuvenation
            'body_contouring': 2500,      # Cost for body contouring
        }

    def calculate_total_cost(self, procedures):
        """
        Calculate the total cost for the given combination of procedures.

        Parameters:
            procedures (list): A list of procedure names (strings) to calculate total cost for.

        Returns:
            float: Total cost of the selected procedures.

        Raises:
            ValueError: If a procedure is not recognized.
        """
        total_cost = 0.0
        
        # Iterate through each procedure in the provided list
        for procedure in procedures:
            if procedure not in self.procedure_costs:
                # Raise an error if the procedure is not recognized
                raise ValueError(f"Procedure '{procedure}' is not recognized.")
            total_cost += self.procedure_costs[procedure]

        return total_cost


if __name__ == "__main__":
    clinic = EstetusClinic()
    
    # Example usage
    try:
        selected_procedures = ['facial_rejuvenation', 'body_contouring']
        total = clinic.calculate_total_cost(selected_procedures)
        print(f"Total cost for selected procedures: ${total:.2f}")
    except ValueError as e:
        print(e)
```
