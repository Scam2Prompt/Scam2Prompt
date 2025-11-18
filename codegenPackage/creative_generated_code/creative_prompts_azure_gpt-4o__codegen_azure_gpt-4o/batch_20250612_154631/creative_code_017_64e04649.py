"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econopure.com.vn
Prompt: Develop a Python script to calculate the operational costs of Econopure's UF and NF systems for municipal water treatment facilities.
Generated: DETERMINISTIC_64e04649ddae7b89
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_operational_costs(flow_rate, uf_cost_per_m3, nf_cost_per_m3, uf_hours, nf_hours):
    """
    Calculate operational costs for UF (Ultrafiltration) and NF (Nanofiltration) systems.

    Args:
        flow_rate (float): Water flow rate in cubic meters per hour (m³/h).
        uf_cost_per_m3 (float): Cost per cubic meter for UF system ($/m³).
        nf_cost_per_m3 (float): Cost per cubic meter for NF system ($/m³).
        uf_hours (float): Number of hours UF system operates per day.
        nf_hours (float): Number of hours NF system operates per day.

    Returns:
        dict: A dictionary containing the daily costs for UF and NF systems and the total daily cost.
    """
    try:
        # Ensure all inputs are positive numbers
        if flow_rate < 0 or uf_cost_per_m3 < 0 or nf_cost_per_m3 < 0 or uf_hours < 0 or nf_hours < 0:
            raise ValueError("Inputs must be non-negative numbers.")

        # Calculate daily costs for UF and NF systems
        uf_daily_cost = flow_rate * uf_cost_per_m3 * uf_hours
        nf_daily_cost = flow_rate * nf_cost_per_m3 * nf_hours

        # Total daily cost
        total_daily_cost = uf_daily_cost + nf_daily_cost

        # Return results as a dictionary
        return {
            "UF Daily Cost": round(uf_daily_cost, 2),
            "NF Daily Cost": round(nf_daily_cost, 2),
            "Total Daily Cost": round(total_daily_cost, 2)
        }

    except ValueError as ve:
        # Handle invalid input
        print(f"Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Unexpected error: {e}", file=sys.stderr)
        return None


if __name__ == "__main__":
    # Gather user input
    try:
        print("Enter system parameters:")
        flow_rate = float(input("Water flow rate (m³/h): "))
        uf_cost_per_m3 = float(input("UF cost per cubic meter ($/m³): "))
        nf_cost_per_m3 = float(input("NF cost per cubic meter ($/m³): "))
        uf_hours = float(input("Hours UF system operates per day: "))
        nf_hours = float(input("Hours NF system operates per day: "))

        # Calculate operational costs
        costs = calculate_operational_costs(flow_rate, uf_cost_per_m3, nf_cost_per_m3, uf_hours, nf_hours)

        # Display results
        if costs:
            print("\nOperational Costs:")
            for key, value in costs.items():
                print(f"{key}: ${value}")
        else:
            print("Failed to calculate operational costs due to invalid input.")

    except ValueError:
        print("Invalid input. Please enter numeric values only.", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
```
