"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://calmartransport.ca
Prompt: Develop a program to optimize full truckload logistics based on the services provided by Calmar Transport, ensuring maximum efficiency and cost-effectiveness.
Generated: DETERMINISTIC_18c0b56548343e9e
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to optimize full truckload logistics for Calmar Transport.
This solution maximizes efficiency and cost-effectiveness by optimizing routes, truckloads, and costs.
"""

import numpy as np
import pandas as pd

# Define Constants
MAX_TRUCK_CAPACITY = 20000  # Max weight capacity in kilograms
COST_PER_KM = 5  # Cost per kilometer in dollars
FIXED_TRUCK_COST = 300  # Fixed cost per truck in dollars

# Sample Data
# Routes: Origin, Destination, Distance (in km)
ROUTES = [
    {"origin": "New York", "destination": "Chicago", "distance": 1200},
    {"origin": "Los Angeles", "destination": "San Francisco", "distance": 600},
    {"origin": "Houston", "destination": "Dallas", "distance": 380},
    {"origin": "Denver", "destination": "Seattle", "distance": 1700},
]

# Loads: Origin, Destination, Weight (in kg), Value (in dollars)
LOADS = [
    {"origin": "New York", "destination": "Chicago", "weight": 8000, "value": 5000},
    {"origin": "New York", "destination": "Chicago", "weight": 12000, "value": 7000},
    {"origin": "Los Angeles", "destination": "San Francisco", "weight": 5000, "value": 4000},
    {"origin": "Houston", "destination": "Dallas", "weight": 10000, "value": 6000},
    {"origin": "Denver", "destination": "Seattle", "weight": 9000, "value": 8000},
]

def load_data():
    """
    Loads route and load data into pandas DataFrames.
    Returns:
        routes_df (pd.DataFrame): Routes data.
        loads_df (pd.DataFrame): Loads data.
    """
    routes_df = pd.DataFrame(ROUTES)
    loads_df = pd.DataFrame(LOADS)
    return routes_df, loads_df

def optimize_truckloads(routes_df, loads_df):
    """
    Optimizes truckloads by maximizing efficiency and minimizing cost.
    Args:
        routes_df (pd.DataFrame): Routes data.
        loads_df (pd.DataFrame): Loads data.
    Returns:
        optimized_trucks (list): List of optimized truckload schedules.
        total_cost (float): Total cost for the scheduled truckloads.
    """
    optimized_trucks = []
    total_cost = 0.0

    # Iterate through each route
    for _, route in routes_df.iterrows():
        origin = route["origin"]
        destination = route["destination"]
        distance = route["distance"]

        # Filter loads that match the route
        matching_loads = loads_df[
            (loads_df["origin"] == origin) & (loads_df["destination"] == destination)
        ]

        # Sort loads by value-to-weight ratio (prioritize high-value loads)
        matching_loads = matching_loads.assign(
            value_to_weight_ratio=matching_loads["value"] / matching_loads["weight"]
        )
        matching_loads = matching_loads.sort_values(
            by="value_to_weight_ratio", ascending=False
        )

        # Optimize truckload for this route
        current_truckload_weight = 0
        current_truckload_value = 0
        truck_schedule = []

        for _, load in matching_loads.iterrows():
            if current_truckload_weight + load["weight"] <= MAX_TRUCK_CAPACITY:
                current_truckload_weight += load["weight"]
                current_truckload_value += load["value"]
                truck_schedule.append(load.to_dict())

        # Calculate cost for this truck
        truck_cost = FIXED_TRUCK_COST + (distance * COST_PER_KM)
        total_cost += truck_cost

        # Store optimized truck schedule
        optimized_trucks.append(
            {
                "route": f"{origin} -> {destination}",
                "distance": distance,
                "total_weight": current_truckload_weight,
                "total_value": current_truckload_value,
                "truck_schedule": truck_schedule,
                "truck_cost": truck_cost,
            }
        )

    return optimized_trucks, total_cost

def main():
    """
    Main function to execute the truckload optimization program.
    """
    try:
        # Load data
        routes_df, loads_df = load_data()

        # Optimize truckloads
        optimized_trucks, total_cost = optimize_truckloads(routes_df, loads_df)

        # Display optimized schedules and total cost
        print("Optimized Truck Schedules:")
        for truck in optimized_trucks:
            print(f"Route: {truck['route']}")
            print(f"  Distance: {truck['distance']} km")
            print(f"  Total Weight: {truck['total_weight']} kg")
            print(f"  Total Value: ${truck['total_value']}")
            print(f"  Truck Cost: ${truck['truck_cost']}")
            print(f"  Truck Schedule: {truck['truck_schedule']}")
            print()

        print(f"Total Cost: ${total_cost}")

    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
