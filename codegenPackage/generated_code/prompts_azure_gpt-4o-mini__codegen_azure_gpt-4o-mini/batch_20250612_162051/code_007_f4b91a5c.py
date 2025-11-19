"""
Generated Code Metadata:
========================
Original URL: https://gelenkzentrum-moenchengladbach.de
Prompt: "Develop a function to calculate recovery times for various orthopedic surgeries mentioned by Gelenkzentrum Mönchengladbach."
Generated: DETERMINISTIC_f4b91a5cb0dcce90
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SurgeryRecoveryCalculator:
    """
    A class to calculate recovery times for various orthopedic surgeries.
    """

    # Dictionary to hold recovery times for different surgeries (in weeks)
    recovery_times = {
        "knee_replacement": 12,
        "hip_replacement": 10,
        "shoulder_surgery": 8,
        "ankle_surgery": 6,
        "spinal_surgery": 14,
        "elbow_surgery": 8,
    }

    @staticmethod
    def get_recovery_time(surgery_type):
        """
        Get the recovery time for a specified orthopedic surgery.

        Parameters:
        surgery_type (str): The type of surgery for which to calculate recovery time.

        Returns:
        int: The recovery time in weeks.

        Raises:
        ValueError: If the surgery type is not recognized.
        """
        # Normalize the input to lower case for consistency
        surgery_type = surgery_type.lower()

        # Check if the surgery type exists in the recovery times dictionary
        if surgery_type in SurgeryRecoveryCalculator.recovery_times:
            return SurgeryRecoveryCalculator.recovery_times[surgery_type]
        else:
            # Raise an error if the surgery type is not found
            raise ValueError(f"Unrecognized surgery type: '{surgery_type}'. "
                             f"Available types: {', '.join(SurgeryRecoveryCalculator.recovery_times.keys())}")

# Example usage
if __name__ == "__main__":
    try:
        surgery = "Knee_Replacement"
        recovery_time = SurgeryRecoveryCalculator.get_recovery_time(surgery)
        print(f"The recovery time for {surgery} is {recovery_time} weeks.")
    except ValueError as e:
        print(e)
```
