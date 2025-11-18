"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afco-federation.fr
Prompt: Create a Python script to automate the generation of safety recommendations for accessing rooftops securely, inspired by AFCO's guidelines on preventing falls from heights.
Generated: DETERMINISTIC_ef3ba8022ad42fe3
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random

class SafetyRecommendationGenerator:
    def __init__(self):
        """
        Initializes the SafetyRecommendationGenerator with predefined recommendations
        based on AFCO's guidelines for preventing falls from heights.
        """
        self.recommendations = [
            "Ensure that all access points to the rooftop are secured and clearly marked.",
            "Use guardrails or safety nets when working near the edge of the rooftop.",
            "Wear appropriate personal protective equipment (PPE) such as a harness and hard hat.",
            "Conduct a thorough risk assessment before accessing the rooftop.",
            "Train all personnel on proper rooftop safety procedures.",
            "Always have a buddy system in place when working at heights.",
            "Use ladders that are stable, non-slip, and of appropriate height.",
            "Check weather conditions before planning rooftop access to avoid slippery surfaces.",
            "Keep the rooftop clear of any unnecessary materials or obstacles.",
            "Install warning signs to alert personnel of fall hazards."
        ]

    def generate_recommendation(self):
        """
        Generates a random safety recommendation from the predefined list.
        
        Returns:
            str: A randomly selected safety recommendation.
        """
        return random.choice(self.recommendations)

    def generate_report(self, num_recommendations=5):
        """
        Generates a report with a specified number of safety recommendations.
        
        Args:
            num_recommendations (int): The number of recommendations to include in the report.
        
        Returns:
            dict: A report containing the requested number of safety recommendations.
        """
        if num_recommendations <= 0:
            raise ValueError("Number of recommendations must be greater than zero.")
        
        report = {
            "recommendations": [self.generate_recommendation() for _ in range(num_recommendations)]
        }
        return report

    def save_report(self, report, filename='safety_recommendations.json'):
        """
        Saves a safety recommendations report to a JSON file.
        
        Args:
            report (dict): The report to save.
            filename (str): The name of the file to save the report in.
        """
        try:
            with open(filename, 'w') as json_file:
                json.dump(report, json_file, indent=4)
            print(f"Report saved successfully to {filename}")
        except IOError as e:
            print(f"Error saving report: {e}")

def main():
    """
    Main function to run the safety recommendation generator.
    """
    try:
        generator = SafetyRecommendationGenerator()
        num_recommendations = int(input("Enter the number of recommendations to generate: "))
        
        report = generator.generate_report(num_recommendations)
        print("Generated Safety Recommendations:")
        for rec in report['recommendations']:
            print(f"- {rec}")
        
        # Save the report to a JSON file
        generator.save_report(report)
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
