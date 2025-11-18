"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Generate a Python script to calculate the optimal cooler size (in quarts) for a camping trip, using Engel Coolers' specifications for ice retention and storage capacity.
Generated: DETERMINISTIC_1a33886cae505b61
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CoolerCalculator:
    """
    A class to calculate the optimal cooler size based on the number of days for a camping trip
    and the number of people involved. It utilizes Engel Coolers' specifications for ice retention
    and storage capacity.
    """

    # Engel Coolers specifications (in quarts), for example purposes
    ICE_RETENTION_DAYS = {
        40: 5,  # 40 qt cooler retains ice for 5 days
        65: 7,  # 65 qt cooler retains ice for 7 days
        80: 10, # 80 qt cooler retains ice for 10 days
    }

    STORAGE_PER_PERSON = 20  # Average quarts of storage needed per person per day

    def __init__(self, days: int, people: int):
        """
        Initializes the CoolerCalculator with the number of days and people.
        
        :param days: Number of days for the camping trip
        :param people: Number of people on the trip
        """
        if days <= 0:
            raise ValueError("Number of days must be greater than zero.")
        if people <= 0:
            raise ValueError("Number of people must be greater than zero.")

        self.days = days
        self.people = people

    def calculate_storage_needs(self) -> int:
        """
        Calculate the total storage needs based on the number of days and people.
        
        :return: Total storage needs in quarts
        """
        return self.days * self.people * CoolerCalculator.STORAGE_PER_PERSON

    def find_optimal_cooler_size(self) -> int:
        """
        Find the optimal cooler size based on the calculated storage needs.
        
        :return: The optimal cooler size in quarts
        """
        storage_needs = self.calculate_storage_needs()
        optimal_size = None

        for size, retention_days in CoolerCalculator.ICE_RETENTION_DAYS.items():
            if retention_days >= self.days:
                if optimal_size is None or size < optimal_size:
                    optimal_size = size

        if optimal_size is None:
            raise Exception("No cooler size found that meets the ice retention requirements.")

        if optimal_size < storage_needs:
            raise Exception(f"Calculated storage needs of {storage_needs} quarts exceeds "
                            f"the optimal cooler size of {optimal_size} quarts.")

        return optimal_size

def main():
    """
    Main function to execute the CoolerCalculator program.
    """
    try:
        # Example user inputs for days and people
        days = int(input("Enter the number of days for your camping trip: "))
        people = int(input("Enter the number of people going on the trip: "))

        cooler_calculator = CoolerCalculator(days, people)
        optimal_cooler_size = cooler_calculator.find_optimal_cooler_size()

        print(f"The optimal cooler size for your trip is: {optimal_cooler_size} quarts.")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
