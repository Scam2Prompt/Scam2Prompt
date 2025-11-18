"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrium.sk
Prompt: Write Python code to generate a legally binding arbitration clause based on the example provided on the Arbitrium.sk website. Include parameters for specifying the arbitration court and governing law.
Generated: DETERMINISTIC_a515208f19575ff4
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from string import Template

def generate_arbitration_clause(arbitration_court: str, governing_law: str) -> str:
    """
    Generates a legally binding arbitration clause.
    
    Parameters:
        arbitration_court (str): The name of the arbitration court.
        governing_law (str): The governing law to be used in arbitration.
    
    Returns:
        str: A formatted arbitration clause.
    """
    # Template for the arbitration clause
    clause_template = Template(
        "Any dispute, controversy, or claim arising out of or relating to this agreement, "
        "including the breach, termination, or validity thereof, shall be finally resolved by arbitration. "
        "The arbitration shall be administered by $arbitration_court in accordance with its rules in effect "
        "at the time of the arbitration. The governing law of this agreement shall be $governing_law."
    )
    
    try:
        # Substitute parameters into the template
        clause = clause_template.substitute(
            arbitration_court=arbitration_court,
            governing_law=governing_law
        )
        return clause
    except KeyError as e:
        # Handle missing keys in the template substitution
        raise ValueError(f"Missing required substitution key: {e}")

# Example usage with error handling
if __name__ == "__main__":
    try:
        # Example inputs for arbitration court and governing law
        arbitration_court_name = "International Arbitration Center"
        governing_law_name = "the laws of the State of New York"
        
        # Generate the arbitration clause
        arbitration_clause = generate_arbitration_clause(arbitration_court_name, governing_law_name)
        print("Generated Arbitration Clause:")
        print(arbitration_clause)
    except ValueError as error:
        # Handle and print error messages
        print(f"Error: {error}")
    except Exception as unexpected_error:
        # Catch any unexpected exceptions
        print(f"An unexpected error occurred: {unexpected_error}")
```
