"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getsonicsolutions.com
Prompt: Create a function that compares different cleaning methods (ultrasonic, pyrolysis, jet washing) for industrial parts, using criteria outlined in Sonic Solutions' knowledge center.
Generated: DETERMINISTIC_91eb6829a8765fe3
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CleaningMethod:
    """Class to represent a cleaning method for industrial parts."""
    
    def __init__(self, name, effectiveness, cost, time_required, environmental_impact):
        """
        Initialize the cleaning method with its attributes.
        
        :param name: Name of the cleaning method
        :param effectiveness: Effectiveness score (1-10)
        :param cost: Cost in currency units
        :param time_required: Time required for cleaning in minutes
        :param environmental_impact: Environmental impact score (1-10)
        """
        self.name = name
        self.effectiveness = effectiveness
        self.cost = cost
        self.time_required = time_required
        self.environmental_impact = environmental_impact

    def __str__(self):
        """Return a string representation of the cleaning method."""
        return f"{self.name}: Effectiveness={self.effectiveness}, Cost={self.cost}, Time={self.time_required}min, Environmental Impact={self.environmental_impact}"


def compare_cleaning_methods(methods):
    """
    Compare different cleaning methods based on specified criteria.
    
    :param methods: List of CleaningMethod objects to compare
    :return: A string summarizing the comparison results
    """
    if not methods:
        raise ValueError("The methods list cannot be empty.")

    comparison_results = []
    for method in methods:
        comparison_results.append(str(method))
    
    best_effectiveness = max(methods, key=lambda m: m.effectiveness)
    best_cost_effectiveness = min(methods, key=lambda m: m.cost / m.effectiveness)
    quickest_method = min(methods, key=lambda m: m.time_required)
    
    summary = (
        "Comparison of Cleaning Methods:\n"
        + "\n".join(comparison_results) + "\n\n"
        + f"Best Effectiveness: {best_effectiveness.name}\n"
        + f"Best Cost-Effectiveness: {best_cost_effectiveness.name}\n"
        + f"Quickest Method: {quickest_method.name}\n"
    )
    
    return summary


# Example data for cleaning methods based on Sonic Solutions' knowledge center
ultrasonic = CleaningMethod("Ultrasonic", effectiveness=9, cost=300, time_required=30, environmental_impact=7)
pyrolysis = CleaningMethod("Pyrolysis", effectiveness=8, cost=500, time_required=120, environmental_impact=5)
jet_washing = CleaningMethod("Jet Washing", effectiveness=7, cost=200, time_required=45, environmental_impact=6)

# List of cleaning methods to compare
cleaning_methods = [ultrasonic, pyrolysis, jet_washing]

# Running the comparison and printing the results
if __name__ == "__main__":
    try:
        results = compare_cleaning_methods(cleaning_methods)
        print(results)
    except ValueError as e:
        print(f"Error: {e}")
```
