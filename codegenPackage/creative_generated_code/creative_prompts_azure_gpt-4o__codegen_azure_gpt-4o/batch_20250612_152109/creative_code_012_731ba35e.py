"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatmaster.pe
Prompt: Develop a program to recommend the best Parrilla for a picnic, factoring in portability, weight, and meat capacity as described on Meat Master.
Generated: DETERMINISTIC_731ba35ebb196d0f
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to recommend the best Parrilla (grill) for a picnic based on portability, weight, 
and meat capacity using pre-defined data from Meat Master.

Assumptions:
1. Data is provided as a list of dictionaries containing Parrilla details.
2. The recommendation will prioritize lower weight, higher meat capacity, and higher portability scores.
"""

# Import necessary modules
import operator

# Sample data (replace or extend with actual data from Meat Master)
parrillas = [
    {"name": "GrillMaster 3000", "weight": 15, "meat_capacity": 10, "portability": 8},
    {"name": "PortableChef", "weight": 10, "meat_capacity": 8, "portability": 9},
    {"name": "MegaGrill X", "weight": 20, "meat_capacity": 12, "portability": 7},
    {"name": "PicnicPro", "weight": 12, "meat_capacity": 9, "portability": 9},
]

def recommend_parrilla(parrilla_list):
    """
    Recommend the best Parrilla for a picnic based on certain criteria.

    Parameters:
    - parrilla_list: List of dictionaries containing Parrilla details.

    Returns:
    - Dictionary representing the best Parrilla recommendation.
    """
    # Validate input
    if not parrilla_list or not isinstance(parrilla_list, list):
        raise ValueError("Parrilla list must be a non-empty list of dictionaries.")
    
    for parrilla in parrilla_list:
        if not isinstance(parrilla, dict) or \
           not all(key in parrilla for key in ("name", "weight", "meat_capacity", "portability")):
            raise ValueError("Each Parrilla must be a dictionary with 'name', 'weight', 'meat_capacity', and 'portability' keys.")

    # Sort Parrillas based on criteria: prioritize portability (desc), meat capacity (desc), and weight (asc)
    sorted_parrillas = sorted(
        parrilla_list,
        key=lambda p: (p["portability"], p["meat_capacity"], -p["weight"]),
        reverse=True
    )

    # Return the best recommendation (first Parrilla in the sorted list)
    return sorted_parrillas[0]

def main():
    """
    Main function to execute the recommendation logic and display the result.
    """
    try:
        best_parrilla = recommend_parrilla(parrillas)
        print(f"Recommended Parrilla for your picnic: {best_parrilla['name']}")
        print(f"Details: Weight = {best_parrilla['weight']} kg, Meat Capacity = {best_parrilla['meat_capacity']} kg, Portability = {best_parrilla['portability']}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
