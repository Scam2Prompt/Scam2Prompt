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
class Parrilla:
    """
    A class to represent a Parrilla (grill) for picnics.
    
    Attributes:
    name (str): The name of the Parrilla.
    weight (float): The weight of the Parrilla in kilograms.
    meat_capacity (float): The maximum meat capacity in kilograms.
    portability_score (int): A score from 1 to 10 indicating how portable the Parrilla is.
    """
    
    def __init__(self, name: str, weight: float, meat_capacity: float, portability_score: int):
        """
        Initializes a new Parrilla instance.
        
        Parameters:
        name (str): The name of the Parrilla.
        weight (float): The weight of the Parrilla in kilograms.
        meat_capacity (float): The maximum meat capacity in kilograms.
        portability_score (int): A score from 1 to 10 indicating how portable the Parrilla is.
        """
        self.name = name
        self.weight = weight
        self.meat_capacity = meat_capacity
        self.portability_score = portability_score

    def __repr__(self):
        """Returns a string representation of the Parrilla."""
        return f"Parrilla(name={self.name}, weight={self.weight}, meat_capacity={self.meat_capacity}, portability_score={self.portability_score})"

def recommend_parrillas(parrillas: list, max_weight: float, min_portability: int) -> list:
    """
    Recommends the best Parrillas based on weight and portability criteria.
    
    Parameters:
    parrillas (list): A list of Parrilla objects.
    max_weight (float): The maximum weight that can be carried.
    min_portability (int): The minimum portability score required.
    
    Returns:
    list: A list of recommended Parrillas.
    """
    recommended = []
    
    for parrilla in parrillas:
        # Check if the Parrilla meets the weight and portability criteria
        if parrilla.weight <= max_weight and parrilla.portability_score >= min_portability:
            recommended.append(parrilla)
    
    return recommended

# Example Parrilla instances
parrilla_list = [
    Parrilla("Compact Grill", 3.5, 2.0, 9),
    Parrilla("Family Grill", 6.0, 5.0, 6),
    Parrilla("Portable Grill", 2.0, 1.5, 10),
    Parrilla("Heavy Duty Grill", 8.0, 10.0, 5)
]

# User-defined criteria
max_weight = 5.0  # Maximum weight allowed
min_portability = 7  # Minimum portability score required

# Fetch recommended Parrillas
try:
    recommended_parrillas = recommend_parrillas(parrilla_list, max_weight, min_portability)
    
    if not recommended_parrillas:
        print("No suitable Parrillas found based on the provided criteria.")
    else:
        print("Recommended Parrillas for your picnic:")
        for parrilla in recommended_parrillas:
            print(parrilla)
except Exception as e:
    print(f"An error occurred: {e}")
```
