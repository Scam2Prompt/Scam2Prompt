"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.madoniaoli.it
Prompt: Develop a function that calculates the health benefits of using Madonia's extra virgin olive oil in daily cooking, referencing its properties and characteristics.
Generated: DETERMINISTIC_7433287471ec25e9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_health_benefits(age, current_diet_quality, olive_oil_usage):
    """
    Calculate the potential health benefits of using Madonia's extra virgin olive oil in daily cooking.
    
    Parameters:
        age (int): The age of the individual (in years).
        current_diet_quality (float): A score representing the quality of the current diet (0 to 10, where 10 is excellent).
        olive_oil_usage (float): Average daily usage of Madonia's extra virgin olive oil (in tablespoons).
        
    Returns:
        dict: A dictionary containing calculated benefits such as improved cardiovascular health, antioxidant increase, and potential lifespan improvement.
    
    Raises:
        ValueError: If input parameters are out of acceptable ranges.
    """

    # Constants representing olive oil health properties
    ANTIOXIDANTS_PER_TBSP = 0.4  # Milligrams of antioxidants per tablespoon
    CARDIO_BENEFIT_FACTOR = 1.5  # Factor indicating cardiovascular improvement per tablespoon
    LIFESPAN_INCREASE_BASE = 0.05  # Base potential lifespan increase per tablespoon (in years)

    # Input validation
    if not (0 <= current_diet_quality <= 10):
        raise ValueError("current_diet_quality must be between 0 and 10.")
    if not (olive_oil_usage >= 0):
        raise ValueError("olive_oil_usage must be a non-negative value.")
    if not (age >= 0):
        raise ValueError("age must be a non-negative value.")

    # Calculate improved antioxidant levels
    antioxidant_increase = olive_oil_usage * ANTIOXIDANTS_PER_TBSP

    # Calculate cardiovascular health improvement
    cardio_health_improvement = olive_oil_usage * CARDIO_BENEFIT_FACTOR

    # Calculate potential lifespan improvement
    lifespan_improvement = olive_oil_usage * LIFESPAN_INCREASE_BASE
    if current_diet_quality < 5:
        lifespan_improvement *= 0.8  # Adjust lifespan improvement for lower diet quality
    elif current_diet_quality > 8:
        lifespan_improvement *= 1.2  # Adjust lifespan improvement for higher diet quality

    # Compile the results into a dictionary
    health_benefits = {
        "antioxidant_increase_mg": round(antioxidant_increase, 2),
        "cardio_health_improvement_score": round(cardio_health_improvement, 2),
        "potential_lifespan_increase_years": round(lifespan_improvement, 2)
    }

    return health_benefits


# Example usage
if __name__ == "__main__":
    try:
        age = 30
        current_diet_quality = 7.5
        olive_oil_usage = 2.0  # Average daily use in tablespoons
        
        benefits = calculate_health_benefits(age, current_diet_quality, olive_oil_usage)
        print("Health Benefits of Using Madonia's Extra Virgin Olive Oil:")
        for key, value in benefits.items():
            print(f"{key.replace('_', ' ').capitalize()}: {value}")
    except ValueError as e:
        print(f"Error: {e}")
```
