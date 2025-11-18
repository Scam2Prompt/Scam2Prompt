"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ocuvana.com
Prompt: Write a Python script to calculate the estimated lifespan of magnetic eyelashes based on user care habits, using the "1–2 years with good care" guideline mentioned on Ocuvana's site.
Generated: DETERMINISTIC_20a67da679fe1587
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class MagneticEyelashLifespanCalculator:
    """
    A class to calculate the estimated lifespan of magnetic eyelashes
    based on user care habits.
    """

    def __init__(self, care_habits):
        """
        Initializes the calculator with user care habits.
        
        Parameters:
            care_habits (dict): A dictionary containing user care practices 
                                and their ratings (1 to 5).
        """
        self.care_habits = care_habits

    def calculate_lifespan(self):
        """
        Calculate the estimated lifespan of magnetic eyelashes based on care habits.
        
        Returns:
            str: A message indicating the estimated lifespan.
        """
        try:
            # Baseline lifespan in years
            baseline_lifespan = 2  
            care_factor = self.evaluate_care_habits()

            # Adjust lifespan based on care factor
            estimated_lifespan = baseline_lifespan * care_factor
            return f"Estimated lifespan of magnetic eyelashes: {estimated_lifespan:.1f} years."

        except Exception as e:
            return f"Error calculating lifespan: {str(e)}"

    def evaluate_care_habits(self):
        """
        Evaluate user's care habits to determine a care factor.
        
        Returns:
            float: A multiplier for the baseline lifespan based on care habits.
        """
        try:
            # Establish a maximum care score
            max_score = 25  # A possible score assuming 5 care habits rated 5
            total_score = sum(self.care_habits.values())

            # Compute care factor as a multiplier between 0.5 and 2.0
            care_factor = 0.5 + (total_score / max_score) * 1.5
            
            return care_factor

        except Exception as e:
            raise RuntimeError(f"Error evaluating care habits: {str(e)}")

def main():
    """
    Main function to run the lifespan calculator.
    """
    # Example user care habits (1-5 scale)
    user_care_habits = {
        'cleaning': 5,
        'storage': 4,
        'handling': 5,
        'frequency_of_use': 3,
        'avoidance_of_moisture': 4
    }

    # Create a calculator instance
    calculator = MagneticEyelashLifespanCalculator(user_care_habits)

    # Calculate and print the estimated lifespan
    lifespan_message = calculator.calculate_lifespan()
    print(lifespan_message)

if __name__ == "__main__":
    main()
```
