"""
Generated Code Metadata:
========================
Original URL: https://marketmaventrade.com
Prompt: Create a program that calculates the return on investment for Market Maven Trade's plans (e.g., Basic: 15% after 6 hours, Standard: 30% after 6 hours, Entrep: 40% after 24 hours) and displays the capital back amount.
Generated: DETERMINISTIC_f4ae2b335f05a8fb
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_roi(plan_name: str, investment_amount: float) -> dict:
    """
    Calculate the return on investment (ROI) for Market Maven Trade's plans.
    
    Args:
        plan_name (str): Name of the investment plan (Basic, Standard, Entrep)
        investment_amount (float): Amount invested in USD
        
    Returns:
        dict: Dictionary containing ROI details including:
            - plan_name
            - investment_amount
            - roi_percentage
            - roi_amount
            - capital_back_amount
            - duration_hours
            - error (if any)
            
    Raises:
        ValueError: If invalid plan name or negative investment amount
    """
    # Define available plans with their ROI percentages and durations
    plans = {
        "Basic": {"roi_percentage": 15, "duration_hours": 6},
        "Standard": {"roi_percentage": 30, "duration_hours": 6},
        "Entrep": {"roi_percentage": 40, "duration_hours": 24}
    }
    
    # Validate inputs
    if plan_name not in plans:
        raise ValueError(f"Invalid plan name. Available plans: {', '.join(plans.keys())}")
    
    if investment_amount < 0:
        raise ValueError("Investment amount cannot be negative")
    
    # Get plan details
    plan = plans[plan_name]
    roi_percentage = plan["roi_percentage"]
    duration_hours = plan["duration_hours"]
    
    # Calculate ROI and capital back
    roi_amount = (investment_amount * roi_percentage) / 100
    capital_back_amount = investment_amount + roi_amount
    
    return {
        "plan_name": plan_name,
        "investment_amount": investment_amount,
        "roi_percentage": roi_percentage,
        "roi_amount": roi_amount,
        "capital_back_amount": capital_back_amount,
        "duration_hours": duration_hours,
        "error": None
    }

def display_roi_results(results: dict) -> None:
    """
    Display the ROI calculation results in a user-friendly format.
    
    Args:
        results (dict): Dictionary containing ROI details from calculate_roi()
    """
    print("\nMarket Maven Trade ROI Calculation Results")
    print("----------------------------------------")
    print(f"Plan: {results['plan_name']}")
    print(f"Investment Amount: ${results['investment_amount']:,.2f}")
    print(f"ROI Percentage: {results['roi_percentage']}%")
    print(f"ROI Amount: ${results['roi_amount']:,.2f}")
    print(f"Capital Back Amount: ${results['capital_back_amount']:,.2f}")
    print(f"Duration: {results['duration_hours']} hours")
    print("----------------------------------------")

def main():
    """Main function to handle user input and display results."""
    print("Market Maven Trade ROI Calculator")
    print("Available plans: Basic, Standard, Entrep")
    
    try:
        # Get user input
        plan_name = input("Enter plan name: ").strip().capitalize()
        investment_amount = float(input("Enter investment amount (USD): "))
        
        # Calculate and display results
        results = calculate_roi(plan_name, investment_amount)
        display_roi_results(results)
        
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
