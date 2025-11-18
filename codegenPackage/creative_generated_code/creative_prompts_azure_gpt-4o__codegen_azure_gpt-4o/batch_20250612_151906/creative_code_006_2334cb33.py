"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boostrunning.com
Prompt: Develop a Python script to analyze running endurance factors (e.g., aerobic capacity, lactate threshold, muscular strength) and suggest training improvements based on Boost Running's guide.
Generated: DETERMINISTIC_2334cb3348f2dcc9
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Constants for endurance factor thresholds based on Boost Running's guide
ENDURANCE_FACTORS = {
    "aerobic_capacity": {"low": 40, "medium": 60, "high": 80},  # VO2 max ranges
    "lactate_threshold": {"low": 50, "medium": 70, "high": 85},  # % of max heart rate
    "muscular_strength": {"low": 20, "medium": 40, "high": 60},  # Relative score
}

# Suggested training improvements based on factor levels
TRAINING_SUGGESTIONS = {
    "aerobic_capacity": {
        "low": "Increase weekly mileage gradually and include low-intensity, long runs.",
        "medium": "Introduce tempo runs and interval training to improve efficiency.",
        "high": "Focus on race-specific training and recovery optimization.",
    },
    "lactate_threshold": {
        "low": "Perform threshold runs at steady discomfort pace to boost tolerance.",
        "medium": "Add hill repeats and fartlek workouts to refine threshold.",
        "high": "Incorporate tapering and race simulations for peak performance.",
    },
    "muscular_strength": {
        "low": "Include bodyweight exercises, plyometrics, and core strengthening.",
        "medium": "Increase resistance training with weights or bands.",
        "high": "Focus on maintaining strength while preventing overtraining.",
    },
}

def analyze_endurance_factors(user_data):
    """
    Analyze running endurance factors and provide training suggestions.
    
    :param user_data: Dictionary containing user's endurance factor scores.
                      Example: {'aerobic_capacity': 45, 'lactate_threshold': 65, 'muscular_strength': 35}
    :return: Dictionary containing training suggestions for each factor.
    """
    suggestions = {}

    for factor, score in user_data.items():
        if factor not in ENDURANCE_FACTORS:
            raise ValueError(f"Invalid factor '{factor}' provided in user data.")
        
        thresholds = ENDURANCE_FACTORS[factor]
        
        if score < thresholds["low"]:
            level = "low"
        elif score < thresholds["medium"]:
            level = "medium"
        else:
            level = "high"
        
        suggestions[factor] = TRAINING_SUGGESTIONS[factor][level]
    
    return suggestions


def main():
    """
    Main function to run the program.
    Collects user input, analyzes endurance factors, and displays training suggestions.
    """
    print("Welcome to the Running Endurance Analyzer!")
    print("Please provide your scores for the following factors:")

    user_data = {}
    for factor in ENDURANCE_FACTORS.keys():
        while True:
            try:
                score = float(input(f"Enter your score for {factor} (0-100): "))
                if 0 <= score <= 100:
                    user_data[factor] = score
                    break
                else:
                    print("Please enter a valid score between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    try:
        # Analyze endurance factors and provide training suggestions
        suggestions = analyze_endurance_factors(user_data)
        
        print("\nTraining Suggestions:")
        for factor, suggestion in suggestions.items():
            print(f"- {factor.capitalize()}: {suggestion}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print("\nThank you for using the Running Endurance Analyzer!")


if __name__ == "__main__":
    main()
```
