"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eagle-tex.cn
Prompt: Write a function in Python to calculate the best fabric options for leggings using Shaoxing Eagles Textile Co., Ltd.'s product data, including "single jacquard knit" and "RT Hacci Jersey."
Generated: DETERMINISTIC_f23338463cd3af3a
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for debugging and error reporting
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Fabric:
    """
    A class to represent fabric details.

    Attributes:
        name (str): Name of the fabric
        weight (float): Weight of the fabric in GSM (grams per square meter)
        stretch_percentage (float): Stretch percentage of the fabric
    """
    def __init__(self, name, weight, stretch_percentage):
        self.name = name
        self.weight = weight
        self.stretch_percentage = stretch_percentage

    def __str__(self):
        return f"{self.name} (Weight: {self.weight} GSM, Stretch: {self.stretch_percentage}%)"


def get_best_fabric_for_leggings(fabric_data):
    """
    Function to calculate the best fabric options for leggings.

    Args:
        fabric_data (list of Fabric): List of Fabric objects containing fabric data.

    Returns:
        list of Fabric: List of recommended fabrics for leggings.
    """
    try:
        if not fabric_data:
            raise ValueError("Fabric data list is empty. Please provide valid fabric data.")

        # Define criteria for "best fabric" for leggings
        # Leggings should use fabrics with moderate to high stretch (>50%) and medium weight (~200-300 GSM)
        RECOMMENDED_WEIGHT_LOWER = 200
        RECOMMENDED_WEIGHT_UPPER = 300
        RECOMMENDED_STRETCH_THRESHOLD = 50

        recommended_fabrics = []
        for fabric in fabric_data:
            # Check if fabric matches the criteria
            if (RECOMMENDED_WEIGHT_LOWER <= fabric.weight <= RECOMMENDED_WEIGHT_UPPER and
                    fabric.stretch_percentage >= RECOMMENDED_STRETCH_THRESHOLD):
                recommended_fabrics.append(fabric)

        if not recommended_fabrics:
            logging.info("No fabrics match the criteria for leggings.")
        return recommended_fabrics

    except Exception as e:
        logging.error(f"An error occurred while calculating the best fabric options: {e}")
        return []


# Example usage
if __name__ == "__main__":
    # Sample fabric data from Shaoxing Eagles Textile Co., Ltd.
    fabric_samples = [
        Fabric("Single Jacquard Knit", 250, 65),
        Fabric("RT Hacci Jersey", 180, 40),
        Fabric("Stretch Nylon Spandex", 220, 70),
        Fabric("Cotton Interlock", 300, 30)
    ]

    best_fabrics = get_best_fabric_for_leggings(fabric_samples)

    if best_fabrics:
        print("Recommended fabrics for leggings:")
        for fabric in best_fabrics:
            print(fabric)
    else:
        print("No suitable fabrics found.")
```
