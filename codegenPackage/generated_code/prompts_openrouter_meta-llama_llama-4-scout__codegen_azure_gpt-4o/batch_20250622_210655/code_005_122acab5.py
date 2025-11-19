"""
Generated Code Metadata:
========================
Original URL: https://erpify.co
Prompt: Generate a Dynamics AX supply chain optimization solution using a Python library.
Generated: DETERMINISTIC_122acab5d0d58603
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
Supply Chain Optimization Solution using Python
This script uses the PuLP library to optimize supply chain operations.
PuLP is a linear programming library in Python that allows us to define and solve optimization problems.
"""

# Import necessary libraries
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, PulpSolverError

def optimize_supply_chain(supply, demand, costs):
    """
    Optimizes supply chain operations by minimizing transportation costs.

    Parameters:
        supply (dict): A dictionary where keys are supply locations and values are their capacities.
        demand (dict): A dictionary where keys are demand locations and values are their requirements.
        costs (dict): A dictionary of dictionaries where costs[supply][demand] represents the cost of transporting
                      from a supply location to a demand location.

    Returns:
        dict: A dictionary containing the optimized transportation plan.
    """
    try:
        # Create the optimization problem
        problem = LpProblem("Supply_Chain_Optimization", LpMinimize)

        # Define decision variables
        transport_vars = {
            (s, d): LpVariable(f"transport_{s}_{d}", lowBound=0, cat="Continuous")
            for s in supply for d in demand
        }

        # Objective function: Minimize transportation costs
        problem += lpSum(transport_vars[s, d] * costs[s][d] for s in supply for d in demand), "Total_Transportation_Cost"

        # Supply constraints: Total outgoing shipments from each supply location cannot exceed its capacity
        for s in supply:
            problem += lpSum(transport_vars[s, d] for d in demand) <= supply[s], f"Supply_Constraint_{s}"

        # Demand constraints: Total incoming shipments to each demand location must meet its requirement
        for d in demand:
            problem += lpSum(transport_vars[s, d] for s in supply) == demand[d], f"Demand_Constraint_{d}"

        # Solve the problem
        problem.solve()

        # Check if the solution is optimal
        if problem.status != 1:  # 1 corresponds to "Optimal"
            raise PulpSolverError("No optimal solution found.")

        # Extract the results
        result = {
            (s, d): transport_vars[s, d].value()
            for s in supply for d in demand
        }

        return result

    except PulpSolverError as e:
        print(f"Error solving the optimization problem: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Define supply capacities
    supply = {
        "Factory_A": 100,
        "Factory_B": 150,
    }

    # Define demand requirements
    demand = {
        "Warehouse_X": 80,
        "Warehouse_Y": 120,
    }

    # Define transportation costs
    costs = {
        "Factory_A": {"Warehouse_X": 2, "Warehouse_Y": 3},
        "Factory_B": {"Warehouse_X": 4, "Warehouse_Y": 1},
    }

    # Run the optimization
    optimized_plan = optimize_supply_chain(supply, demand, costs)

    # Display the results
    if optimized_plan:
        print("Optimized Transportation Plan:")
        for (s, d), quantity in optimized_plan.items():
            print(f"Transport {quantity:.2f} units from {s} to {d}")
    else:
        print("Failed to generate an optimized transportation plan.")
```
