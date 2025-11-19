"""
Generated Code Metadata:
========================
Original URL: https://trysonicsolutions.com
Prompt: Explain how ultrasonic cleaning can extend the lifespan of filters in the plastics industry and provide a case study example.
Generated: DETERMINISTIC_652a389ec81bce40
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class UltrasonicCleaner:
    """
    A class to represent an ultrasonic cleaner for filters in the plastics industry.
    """

    def __init__(self, frequency: float, power: float):
        """
        Initializes the ultrasonic cleaner with specified frequency and power.

        :param frequency: Frequency of the ultrasonic waves in kHz.
        :param power: Power of the ultrasonic cleaner in watts.
        """
        self.frequency = frequency
        self.power = power

    def clean_filter(self, filter_type: str, duration: int) -> str:
        """
        Cleans the specified filter using ultrasonic waves.

        :param filter_type: Type of filter to be cleaned.
        :param duration: Duration of cleaning in minutes.
        :return: Status message indicating the result of the cleaning process.
        """
        try:
            if duration <= 0:
                raise ValueError("Duration must be a positive integer.")
            if filter_type not in ["HEPA", "Carbon", "Mesh"]:
                raise ValueError("Invalid filter type. Choose from: HEPA, Carbon, Mesh.")

            # Simulate the cleaning process
            print(f"Cleaning {filter_type} filter for {duration} minutes at {self.frequency} kHz and {self.power} watts.")
            # Here we would have the actual cleaning logic
            return f"{filter_type} filter cleaned successfully."

        except ValueError as e:
            return f"Error: {e}"

    def extend_filter_lifespan(self, filter_type: str) -> str:
        """
        Provides information on how ultrasonic cleaning extends the lifespan of filters.

        :param filter_type: Type of filter to be discussed.
        :return: Explanation of lifespan extension.
        """
        lifespan_extension_info = {
            "HEPA": "Ultrasonic cleaning removes fine particles and contaminants, maintaining airflow and efficiency.",
            "Carbon": "Regular cleaning prevents clogging, ensuring optimal adsorption of odors and gases.",
            "Mesh": "Ultrasonic cleaning dislodges debris, preventing wear and tear on the mesh material."
        }
        
        return lifespan_extension_info.get(filter_type, "No information available for this filter type.")

# Example usage
if __name__ == "__main__":
    cleaner = UltrasonicCleaner(frequency=40.0, power=100.0)

    # Clean a HEPA filter
    result = cleaner.clean_filter("HEPA", 30)
    print(result)

    # Extend lifespan information for a Carbon filter
    lifespan_info = cleaner.extend_filter_lifespan("Carbon")
    print(lifespan_info)

    # Attempt to clean an invalid filter type
    invalid_result = cleaner.clean_filter("InvalidType", 15)
    print(invalid_result)
```
