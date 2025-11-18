"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelinjectorservices.com.au
Prompt: Develop a program that categorizes fuel injectors by type (mechanical, electronic, petrol, diesel) and generates a maintenance schedule based on the cleaning process outlined on the Fuel Injector Services website.
Generated: DETERMINISTIC_7fa7fb60251b861f
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# fuel_injector_manager.py

from enum import Enum
from datetime import datetime, timedelta
import logging

# Set up logging to track the program's execution
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FuelInjectorType(Enum):
    MECHANICAL = "Mechanical"
    ELECTRONIC = "Electronic"
    PETROL = "Petrol"
    DIESEL = "Diesel"

class FuelInjector:
    def __init__(self, injector_type: FuelInjectorType, last_cleaned: datetime):
        """
        Initialize a FuelInjector instance.

        :param injector_type: Type of fuel injector (Mechanical, Electronic, Petrol, Diesel)
        :param last_cleaned: Last cleaned date of the injector
        """
        self.injector_type = injector_type
        self.last_cleaned = last_cleaned

    def schedule_cleaning(self) -> datetime:
        """
        Calculate the next cleaning date based on the injector type.

        :return: Next scheduled cleaning date
        """
        try:
            if self.injector_type in [FuelInjectorType.PETROL, FuelInjectorType.MECHANICAL]:
                cleaning_interval = timedelta(days=180)  # every 6 months
            elif self.injector_type in [FuelInjectorType.DIESEL, FuelInjectorType.ELECTRONIC]:
                cleaning_interval = timedelta(days=365)  # every year
            else:
                raise ValueError(f"Unknown fuel injector type: {self.injector_type}")

            next_cleaning_date = self.last_cleaned + cleaning_interval
            logging.info(f"Next cleaning scheduled for {next_cleaning_date.strftime('%Y-%m-%d')} for {self.injector_type.value} injector.")
            return next_cleaning_date
        
        except Exception as e:
            logging.error(f"Error calculating cleaning schedule: {str(e)}")
            raise

def main():
    # Example usage
    try:
        # Create instances of fuel injectors
        injector1 = FuelInjector(FuelInjectorType.PETROL, datetime(2023, 1, 1))
        injector2 = FuelInjector(FuelInjectorType.DIESEL, datetime(2022, 6, 15))
        injector3 = FuelInjector(FuelInjectorType.ELECTRONIC, datetime(2023, 8, 5))

        # Schedule cleanings
        injector1.schedule_cleaning()
        injector2.schedule_cleaning()
        injector3.schedule_cleaning()

    except Exception as error:
        logging.error(f"An error occurred in the main execution: {str(error)}")

if __name__ == "__main__":
    main()
```
