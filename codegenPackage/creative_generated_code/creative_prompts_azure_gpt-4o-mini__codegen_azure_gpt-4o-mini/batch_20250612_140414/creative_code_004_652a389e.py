"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trysonicsolutions.com
Prompt: Explain how ultrasonic cleaning can extend the lifespan of filters in the plastics industry and provide a case study example.
Generated: DETERMINISTIC_652a389ec81bce40
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# ultrasonic_cleaning.py

class UltrasonicCleaner:
    """
    A class to represent an ultrasonic cleaner for filters in the plastics industry.
    """

    def __init__(self, frequency: float, tank_volume: float):
        """
        Initializes the ultrasonic cleaner with specified frequency and tank volume.

        :param frequency: Frequency of ultrasonic waves in kHz
        :param tank_volume: Volume of the cleaning tank in liters
        """
        self.frequency = frequency
        self.tank_volume = tank_volume

    def clean_filter(self, filter_id: str):
        """
        Simulates the cleaning process of a filter using ultrasonic waves.

        :param filter_id: Unique identifier for the filter being cleaned
        :raises ValueError: If the filter_id is empty or None
        """
        if not filter_id:
            raise ValueError("Filter ID must be a valid non-empty string.")
        
        print(f"Starting ultrasonic cleaning process for filter ID: {filter_id}")
        self.perform_cleaning()
        print(f"Cleaning process completed for filter ID: {filter_id}")

    def perform_cleaning(self):
        """
        Performs the actual cleaning process. This is a placeholder for the cleaning logic.
        """
        # Simulate cleaning duration
        import time
        time.sleep(2)  # Simulating time taken for cleaning
        print(f"Cleaning completed at frequency of {self.frequency} kHz in a {self.tank_volume}L tank.")

def case_study():
    """
    A case study example demonstrating the effect of ultrasonic cleaning on filter lifespan.
    """
    print("Case Study: Extending Filter Lifespan with Ultrasonic Cleaning")

    # Create an instance of UltrasonicCleaner
    cleaner = UltrasonicCleaner(frequency=40.0, tank_volume=50.0)

    # Simulate cleaning a filter
    filter_id = "FILTER-001"
    print(f"Initial filter condition for {filter_id}: Clogged")
    cleaner.clean_filter(filter_id)

    # Simulate improved filter condition
    print(f"Post cleaning condition for {filter_id}: Clean and functional")
    print("Conclusion: Ultrasonic cleaning has significantly improved the performance and lifespan of the filter.")

if __name__ == "__main__":
    try:
        case_study()
    except Exception as e:
        print(f"An error occurred: {e}")
```
