"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gelenkzentrum-moenchengladbach.de
Prompt: "Develop a function to calculate recovery times for various orthopedic surgeries mentioned by Gelenkzentrum Mönchengladbach."
Generated: DETERMINISTIC_f4b91a5cb0dcce90
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class SurgeryRecoveryTimeCalculator:
    """
    A class to calculate recovery times for various orthopedic surgeries.
    """

    def __init__(self):
        # Dictionary to store recovery times for different surgeries (in days)
        self.surgery_recovery_times = {
            "knee_replacement": 90,
            "hip_replacement": 90,
            "shoulder_replacement": 120,
            "ACL_reconstruction": 180,
            "meniscus_repair": 60,
            "fracture_fixation": 45
        }

    def get_recovery_time(self, surgery_type):
        """
        Get the recovery time for a specific surgery type.

        Parameters:
        surgery_type (str): The type of surgery.

        Returns:
        int: The recovery time in days.

        Raises:
        ValueError: If the surgery type is not recognized.
        """
        try:
            # Normalize the input to lower case to handle case insensitivity
            surgery_type_normalized = surgery_type.lower()
            if surgery_type_normalized not in self.surgery_recovery_times:
                raise ValueError(f"Unrecognized surgery type: {surgery_type}")

            return self.surgery_recovery_times[surgery_type_normalized]
        except Exception as e:
            # Catch any unexpected errors and log them
            print(f"Error occurred while fetching recovery time: {e}")
            raise

    def to_json(self):
        """
        Convert the recovery times to a JSON formatted string.

        Returns:
        str: JSON formatted string of recovery times.
        """
        return json.dumps(self.surgery_recovery_times, indent=4)

if __name__ == "__main__":
    # Example usage:
    calculator = SurgeryRecoveryTimeCalculator()
    
    try:
        surgery_type = "Knee_Replacement"  # Example input
        recovery_time = calculator.get_recovery_time(surgery_type)
        print(f"Recovery time for {surgery_type}: {recovery_time} days")
        
        # Print recovery times in JSON format
        print("All recovery times:")
        print(calculator.to_json())
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
