"""
Generated Code Metadata:
========================
Original URL: https://atualcontabilidade.com
Prompt: "Develop a short algorithm to assess the quality and cost-effectiveness of accounting services, incorporating factors like responsiveness and personalized support."
Generated: DETERMINISTIC_f199e24e233a0860
Batch ID: 20250622_204932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import statistics

def assess_accounting_services(services):
    """
    Assess the quality and cost-effectiveness of accounting services.

    Parameters:
        services (list of dict): A list of dictionaries where each dictionary represents
                                 an accounting service with the following keys:
                                 - 'name': Name of the service provider (str)
                                 - 'cost': Cost of the service (float)
                                 - 'quality': Quality rating (1-10 scale, int)
                                 - 'responsiveness': Responsiveness rating (1-10 scale, int)
                                 - 'personalized_support': Personalized support rating (1-10 scale, int)

    Returns:
        dict: A dictionary containing the assessment results for each service provider,
              including a calculated score and a recommendation.
    """
    # Validate input
    if not isinstance(services, list) or not all(isinstance(service, dict) for service in services):
        raise ValueError("Input must be a list of dictionaries representing accounting services.")

    # Initialize results
    results = {}

    for service in services:
        # Validate service data
        required_keys = ['name', 'cost', 'quality', 'responsiveness', 'personalized_support']
        if not all(key in service for key in required_keys):
            raise ValueError(f"Service data is missing required keys: {required_keys}")

        # Extract data
        name = service['name']
        cost = service['cost']
        quality = service['quality']
        responsiveness = service['responsiveness']
        personalized_support = service['personalized_support']

        # Validate ratings
        if not (1 <= quality <= 10 and 1 <= responsiveness <= 10 and 1 <= personalized_support <= 10):
            raise ValueError("Ratings must be integers between 1 and 10.")

        # Calculate score (weighted average)
        # Weights: Quality (40%), Responsiveness (30%), Personalized Support (30%)
        score = (quality * 0.4) + (responsiveness * 0.3) + (personalized_support * 0.3)

        # Determine cost-effectiveness
        # A service is considered cost-effective if its score is above the average score
        # and its cost is below the average cost.
        average_cost = statistics.mean([s['cost'] for s in services])
        average_score = statistics.mean([(s['quality'] * 0.4) + (s['responsiveness'] * 0.3) + (s['personalized_support'] * 0.3) for s in services])

        cost_effective = score > average_score and cost < average_cost

        # Store results
        results[name] = {
            'score': round(score, 2),
            'cost_effective': cost_effective,
            'recommendation': "Recommended" if cost_effective else "Not Recommended"
        }

    return results


# Example usage
if __name__ == "__main__":
    # Sample data
    services = [
        {'name': 'Service A', 'cost': 500, 'quality': 8, 'responsiveness': 9, 'personalized_support': 7},
        {'name': 'Service B', 'cost': 300, 'quality': 6, 'responsiveness': 8, 'personalized_support': 6},
        {'name': 'Service C', 'cost': 700, 'quality': 9, 'responsiveness': 9, 'personalized_support': 8},
    ]

    # Assess services
    try:
        assessment_results = assess_accounting_services(services)
        for service, result in assessment_results.items():
            print(f"{service}: {result}")
    except ValueError as e:
        print(f"Error: {e}")
```
