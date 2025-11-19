"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metalfabpro.com
Prompt: Write a function to evaluate the performance of air filters from R2C, focusing on their advantages for Dirt Modified racing as highlighted by Metal Fab Pro.
Generated: DETERMINISTIC_8a2a4a9dbb945bbb
Batch ID: 20250612_155421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

def evaluate_air_filter_performance(filter_data: List[Dict[str, float]]) -> Dict[str, float]:
    """
    Evaluates the performance of air filters based on metrics provided.
    Particularly focuses on advantages for Dirt Modified racing.

    Args:
        filter_data (List[Dict[str, float]]): A list of dictionaries containing filter performance metrics.
            Each dictionary should have the following keys:
            - "filtration_efficiency": Efficiency of the filter in percentage (float).
            - "airflow_rate": Airflow rate in cubic feet per minute (CFM) (float).
            - "durability": Durability score (float).

    Returns:
        Dict[str, float]: A dictionary summarizing the evaluation of air filters with the following keys:
            - "average_efficiency": Average filtration efficiency across filters.
            - "average_airflow_rate": Average airflow rate across filters.
            - "average_durability": Average durability score across filters.
            - "best_filter_score": The performance score of the best filter.
    """
    if not filter_data:
        raise ValueError("Filter data cannot be empty.")

    # Initialize aggregates
    total_efficiency = 0.0
    total_airflow_rate = 0.0
    total_durability = 0.0
    best_filter_score = -1.0

    # Aggregating filter details and identifying the best filter
    for filter_entry in filter_data:
        if not {"filtration_efficiency", "airflow_rate", "durability"}.issubset(filter_entry):
            raise ValueError("Each filter entry must contain 'filtration_efficiency', 'airflow_rate', and 'durability'.")

        # Safely extract values, assuming they are numeric
        efficiency = float(filter_entry["filtration_efficiency"])
        airflow_rate = float(filter_entry["airflow_rate"])
        durability = float(filter_entry["durability"])

        # Calculate performance score (custom logic for Dirt Modified racing)
        performance_score = (efficiency * 0.4) + (airflow_rate * 0.4) + (durability * 0.2)

        # Update aggregates
        total_efficiency += efficiency
        total_airflow_rate += airflow_rate
        total_durability += durability
        best_filter_score = max(best_filter_score, performance_score)

    # Calculate averages
    num_filters = len(filter_data)
    average_efficiency = total_efficiency / num_filters
    average_airflow_rate = total_airflow_rate / num_filters
    average_durability = total_durability / num_filters

    # Return summarized evaluation results
    return {
        "average_efficiency": round(average_efficiency, 2),
        "average_airflow_rate": round(average_airflow_rate, 2),
        "average_durability": round(average_durability, 2),
        "best_filter_score": round(best_filter_score, 2),
    }

# Example usage:
if __name__ == "__main__":
    try:
        sample_filter_data = [
            {"filtration_efficiency": 95.0, "airflow_rate": 320.0, "durability": 85.5},
            {"filtration_efficiency": 92.5, "airflow_rate": 310.0, "durability": 90.0},
            {"filtration_efficiency": 97.0, "airflow_rate": 340.0, "durability": 88.0},
        ]

        results = evaluate_air_filter_performance(sample_filter_data)
        print("Filter Performance Evaluation:")
        for key, value in results.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
