"""
Generated Code Metadata:
========================
Original URL: https://thehashtagconsultants.com
Prompt: "Write a Python script to calculate the cost savings of outsourcing customer support to a BPO provider like The Hashtag Consultants, considering factors such as hourly agent costs and facility expenses."
Generated: DETERMINISTIC_08305128edda6e24
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
BPO Cost Savings Calculator

This script calculates the cost savings of outsourcing customer support to a BPO provider
by comparing in-house costs vs BPO costs. It considers factors like hourly agent rates,
facility expenses, and other operational costs.

Usage:
    python bpo_cost_savings.py
"""

import argparse
from typing import Dict, Union

def calculate_cost_savings(
    in_house_agent_hourly: float,
    bpo_agent_hourly: float,
    agents_count: int,
    operating_hours: float,
    in_house_facility_cost: float,
    bpo_facility_cost: float,
    in_house_other_costs: float = 0,
    bpo_other_costs: float = 0
) -> Dict[str, Union[float, Dict[str, float]]]:
    """
    Calculate cost savings from outsourcing customer support to a BPO provider.

    Args:
        in_house_agent_hourly: Hourly cost per in-house agent (USD)
        bpo_agent_hourly: Hourly cost per BPO agent (USD)
        agents_count: Number of agents
        operating_hours: Monthly operating hours per agent
        in_house_facility_cost: Monthly facility cost for in-house (USD)
        bpo_facility_cost: Monthly facility cost for BPO (USD)
        in_house_other_costs: Other monthly in-house costs (USD)
        bpo_other_costs: Other monthly BPO costs (USD)

    Returns:
        Dictionary containing cost breakdown and savings analysis
    """
    # Calculate labor costs
    in_house_labor = in_house_agent_hourly * agents_count * operating_hours
    bpo_labor = bpo_agent_hourly * agents_count * operating_hours

    # Calculate total costs
    in_house_total = in_house_labor + in_house_facility_cost + in_house_other_costs
    bpo_total = bpo_labor + bpo_facility_cost + bpo_other_costs

    # Calculate savings
    savings = in_house_total - bpo_total
    savings_percentage = (savings / in_house_total) * 100 if in_house_total > 0 else 0

    return {
        "cost_breakdown": {
            "in_house": {
                "labor": in_house_labor,
                "facility": in_house_facility_cost,
                "other": in_house_other_costs,
                "total": in_house_total
            },
            "bpo": {
                "labor": bpo_labor,
                "facility": bpo_facility_cost,
                "other": bpo_other_costs,
                "total": bpo_total
            }
        },
        "savings": {
            "amount": savings,
            "percentage": savings_percentage
        }
    }

def format_currency(amount: float) -> str:
    """Format a number as USD currency."""
    return f"${amount:,.2f}"

def display_results(results: Dict[str, Union[float, Dict[str, float]]]) -> None:
    """Display the cost savings analysis in a readable format."""
    breakdown = results["cost_breakdown"]
    savings = results["savings"]

    print("\n=== Cost Savings Analysis ===")
    print("\nIn-House Costs:")
    print(f"  Labor: {format_currency(breakdown['in_house']['labor'])}")
    print(f"  Facility: {format_currency(breakdown['in_house']['facility'])}")
    print(f"  Other: {format_currency(breakdown['in_house']['other'])}")
    print(f"  Total: {format_currency(breakdown['in_house']['total'])}")

    print("\nBPO Costs:")
    print(f"  Labor: {format_currency(breakdown['bpo']['labor'])}")
    print(f"  Facility: {format_currency(breakdown['bpo']['facility'])}")
    print(f"  Other: {format_currency(breakdown['bpo']['other'])}")
    print(f"  Total: {format_currency(breakdown['bpo']['total'])}")

    print("\nSavings:")
    print(f"  Amount: {format_currency(savings['amount'])}")
    print(f"  Percentage: {savings['percentage']:.2f}%")

def validate_input(value: float, name: str) -> None:
    """Validate that input values are non-negative."""
    if value < 0:
        raise ValueError(f"{name} must be a non-negative number")

def main():
    """Main function to handle command-line input and display results."""
    parser = argparse.ArgumentParser(
        description="Calculate cost savings from outsourcing customer support to a BPO provider."
    )
    
    parser.add_argument("--in-house-agent", type=float, required=True,
                       help="Hourly cost per in-house agent (USD)")
    parser.add_argument("--bpo-agent", type=float, required=True,
                       help="Hourly cost per BPO agent (USD)")
    parser.add_argument("--agents", type=int, required=True,
                       help="Number of agents")
    parser.add_argument("--hours", type=float, required=True,
                       help="Monthly operating hours per agent")
    parser.add_argument("--in-house-facility", type=float, required=True,
                       help="Monthly facility cost for in-house (USD)")
    parser.add_argument("--bpo-facility", type=float, required=True,
                       help="Monthly facility cost for BPO (USD)")
    parser.add_argument("--in-house-other", type=float, default=0,
                       help="Other monthly in-house costs (USD)")
    parser.add_argument("--bpo-other", type=float, default=0,
                       help="Other monthly BPO costs (USD)")

    try:
        args = parser.parse_args()
        
        # Validate inputs
        validate_input(args.in_house_agent, "In-house agent hourly cost")
        validate_input(args.bpo_agent, "BPO agent hourly cost")
        validate_input(args.agents, "Number of agents")
        validate_input(args.hours, "Operating hours")
        validate_input(args.in_house_facility, "In-house facility cost")
        validate_input(args.bpo_facility, "BPO facility cost")
        validate_input(args.in_house_other, "In-house other costs")
        validate_input(args.bpo_other, "BPO other costs")

        # Calculate and display results
        results = calculate_cost_savings(
            in_house_agent_hourly=args.in_house_agent,
            bpo_agent_hourly=args.bpo_agent,
            agents_count=args.agents,
            operating_hours=args.hours,
            in_house_facility_cost=args.in_house_facility,
            bpo_facility_cost=args.bpo_facility,
            in_house_other_costs=args.in_house_other,
            bpo_other_costs=args.bpo_other
        )
        
        display_results(results)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
