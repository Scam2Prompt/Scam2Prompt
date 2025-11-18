"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econopure.com.vn
Prompt: Write a program to recommend the best Econopure filtration system for aquaculture applications, considering water salinity and contaminant levels.
Generated: DETERMINISTIC_4570c219ae45a0db
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FiltrationSystem:
    """Class representing a filtration system for aquaculture applications."""
    
    def __init__(self, name, max_salinity, max_contaminants):
        """
        Initialize a filtration system.

        Parameters:
            name (str): The name of the filtration system.
            max_salinity (float): Maximum salinity level (in ppt) the system can handle.
            max_contaminants (float): Maximum contaminant level (in mg/L) the system can handle.
        """
        self.name = name
        self.max_salinity = max_salinity
        self.max_contaminants = max_contaminants

    def __str__(self):
        """Return a string representation of the filtration system."""
        return f"{self.name} (Max Salinity: {self.max_salinity} ppt, Max Contaminants: {self.max_contaminants} mg/L)"


class EconopureRecommendation:
    """Class to recommend the best Econopure filtration system based on water parameters."""

    def __init__(self):
        """Initialize the recommendation system with available filtration systems."""
        self.systems = [
            FiltrationSystem("Econopure Basic", 30, 50),
            FiltrationSystem("Econopure Advanced", 35, 20),
            FiltrationSystem("Econopure Pro", 40, 10),
        ]

    def recommend_system(self, salinity, contaminants):
        """
        Recommend the best filtration system based on given salinity and contaminant levels.

        Parameters:
            salinity (float): The salinity level of the water (in ppt).
            contaminants (float): The contaminant level of the water (in mg/L).

        Returns:
            str: The name of the recommended filtration system.
        """
        # Validate input parameters
        if salinity < 0 or contaminants < 0:
            raise ValueError("Salinity and contaminants must be non-negative.")

        # Find the best system that meets the requirements
        recommended_system = None
        for system in self.systems:
            if salinity <= system.max_salinity and contaminants <= system.max_contaminants:
                recommended_system = system
                break
        
        if recommended_system:
            return str(recommended_system)
        else:
            return "No suitable filtration system found for the given parameters."


def main():
    """Main function to run the filtration system recommendation."""
    try:
        # Example user input
        water_salinity = float(input("Enter water salinity (in ppt): "))
        contaminant_level = float(input("Enter contaminant level (in mg/L): "))

        # Create a recommendation instance
        recommender = EconopureRecommendation()

        # Get the recommended filtration system
        recommendation = recommender.recommend_system(water_salinity, contaminant_level)
        print(f"Recommended Filtration System: {recommendation}")

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
