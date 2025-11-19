"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dee-lance.pages.dev
Prompt: Write a script to compare the fees of DeeLance with traditional hiring platforms, highlighting the benefits of using DeeLance.
Generated: DETERMINISTIC_5a8266ad8c60c45a
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to compare the fees of DeeLance with traditional hiring platforms.
Highlights the cost benefits of using DeeLance.

Assumptions:
- DeeLance charges a flat fee percentage (e.g., 10%) on project cost.
- Traditional hiring platforms charge a higher fee percentage (e.g., 20%) on project cost.
- Inputs: Project cost, DeeLance fee percentage, traditional platform fee percentage.
"""

def calculate_fee(project_cost, fee_percentage):
    """
    Calculate the fee based on the project cost and fee percentage.

    Args:
        project_cost (float): The total cost of the project.
        fee_percentage (float): The fee percentage charged by the platform.

    Returns:
        float: The calculated fee amount.
    """
    try:
        # Ensure inputs are positive numbers
        if project_cost < 0 or fee_percentage < 0:
            raise ValueError("Project cost and fee percentage must be positive numbers.")
        
        # Calculate and return the fee
        return project_cost * (fee_percentage / 100)
    except TypeError:
        raise TypeError("Invalid input types. Ensure project_cost and fee_percentage are numbers.")

def compare_fees(project_cost, deelance_fee_percentage, traditional_fee_percentage):
    """
    Compare the fees of DeeLance with traditional hiring platforms.

    Args:
        project_cost (float): The total cost of the project.
        deelance_fee_percentage (float): DeeLance's fee percentage.
        traditional_fee_percentage (float): Traditional platform's fee percentage.

    Returns:
        dict: A dictionary containing the fee comparison details.
    """
    try:
        # Calculate fees for both platforms
        deelance_fee = calculate_fee(project_cost, deelance_fee_percentage)
        traditional_fee = calculate_fee(project_cost, traditional_fee_percentage)

        # Calculate savings with DeeLance
        savings = traditional_fee - deelance_fee

        # Return fee comparison details
        return {
            "project_cost": project_cost,
            "deelance_fee": deelance_fee,
            "traditional_fee": traditional_fee,
            "savings_with_deelance": savings
        }
    except Exception as error:
        raise RuntimeError(f"An error occurred while comparing fees: {error}")

def main():
    """
    Main function to run the fee comparison script.
    """
    try:
        # Input values (can be replaced with dynamic inputs or user prompts)
        project_cost = 5000.0  # Example project cost in USD
        deelance_fee_percentage = 10.0  # DeeLance charges 10%
        traditional_fee_percentage = 20.0  # Traditional platforms charge 20%

        # Compare fees
        comparison_results = compare_fees(project_cost, deelance_fee_percentage, traditional_fee_percentage)

        # Display results
        print("Fee Comparison Results:")
        print(f"Project Cost: ${comparison_results['project_cost']:.2f}")
        print(f"DeeLance Fee: ${comparison_results['deelance_fee']:.2f}")
        print(f"Traditional Platform Fee: ${comparison_results['traditional_fee']:.2f}")
        print(f"Savings with DeeLance: ${comparison_results['savings_with_deelance']:.2f}")
    except Exception as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
```
