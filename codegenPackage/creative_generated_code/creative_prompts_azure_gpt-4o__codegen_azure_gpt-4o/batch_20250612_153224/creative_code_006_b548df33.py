"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munasimkullakita.org
Prompt: Develop a recommendation system that suggests appropriate social programs for vulnerable populations based on their age, risk level, and geographic location, inspired by Fundación Munasim Kullakita's methodologies.
Generated: DETERMINISTIC_b548df332bb8c7f8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class RecommendationSystem:
    """
    A system to recommend social programs for vulnerable populations based on their age, 
    risk level, and geographic location.
    """

    def __init__(self, program_data_file):
        """
        Initialize the recommendation system with social program data.

        :param program_data_file: Path to the JSON file containing program data.
        """
        try:
            with open(program_data_file, 'r') as file:
                self.programs = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("Program data file not found. Please provide a valid file path.")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in the program data file.")

    def recommend_programs(self, age, risk_level, location):
        """
        Recommend appropriate social programs based on age, risk level, and geographic location.

        :param age: Age of the individual (integer).
        :param risk_level: Risk level of the individual (e.g., "low", "medium", "high").
        :param location: Geographic location of the individual (string).
        :return: List of recommended programs.
        """
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a non-negative integer.")

        if risk_level not in ["low", "medium", "high"]:
            raise ValueError("Risk level must be one of ['low', 'medium', 'high'].")

        if not isinstance(location, str) or not location.strip():
            raise ValueError("Location must be a non-empty string.")

        recommendations = []

        # Iterate through programs and determine suitability based on criteria
        for program in self.programs:
            program_age_range = program.get("age_range", [])
            program_risk_levels = program.get("risk_levels", [])
            program_locations = program.get("locations", [])

            if (program_age_range[0] <= age <= program_age_range[1] and
                    risk_level in program_risk_levels and
                    location.lower() in map(str.lower, program_locations)):
                recommendations.append(program)

        return recommendations


if __name__ == "__main__":
    # Sample program data file path
    PROGRAM_DATA_FILE = "social_programs.json"

    try:
        # Instantiate the recommendation system
        system = RecommendationSystem(PROGRAM_DATA_FILE)

        # Example inputs
        age = 25
        risk_level = "medium"
        location = "La Paz"

        # Get recommendations
        recommended_programs = system.recommend_programs(age, risk_level, location)

        # Display results
        if recommended_programs:
            print("Recommended Social Programs:")
            for program in recommended_programs:
                print(f"- {program['name']} ({program['description']})")
        else:
            print("No programs found matching the criteria.")

    except Exception as e:
        print(f"Error: {e}")
```

**Sample `social_programs.json` file**:
```json
[
    {
        "name": "Youth Support Program",
        "description": "Provides educational and emotional support for at-risk youth.",
        "age_range": [12, 25],
        "risk_levels": ["medium", "high"],
        "locations": ["La Paz", "El Alto"]
    },
    {
        "name": "Elderly Assistance Initiative",
        "description": "Offers healthcare and social activities for elderly individuals.",
        "age_range": [60, 100],
        "risk_levels": ["low", "medium"],
        "locations": ["Santa Cruz", "La Paz"]
    },
    {
        "name": "Women's Empowerment Program",
        "description": "Supports women with skills training and resources for independence.",
        "age_range": [18, 50],
        "risk_levels": ["medium", "high"],
        "locations": ["Cochabamba", "La Paz"]
    }
]
```
