"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.chicoelectric.com
Prompt: Generate code to calculate backup generator reliability and maintenance schedules, referencing Chico Electric's generator installations for the City of Chico.
Generated: DETERMINISTIC_fc8c21965185e109
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Tuple

class Generator:
    """
    Class representing a backup generator installation.
    """
    def __init__(self, id: int, installation_date: datetime.date, service_interval_days: int):
        """
        Initialize a new Generator instance.

        :param id: Unique identifier for the generator.
        :param installation_date: Date when the generator was installed.
        :param service_interval_days: Recommended maintenance interval in days.
        """
        self.id = id
        self.installation_date = installation_date
        self.service_interval_days = service_interval_days

    def next_service_date(self) -> datetime.date:
        """
        Calculate the next service date based on the installation date and service interval.

        :return: Next service date.
        """
        return self.installation_date + datetime.timedelta(days=self.service_interval_days)

    def reliability_percentage(self, failures: int, total_tests: int) -> float:
        """
        Calculate the reliability percentage of the generator.

        :param failures: Number of failures recorded.
        :param total_tests: Total tests/operations performed.
        :return: Reliability percentage.
        """
        if total_tests == 0:
            raise ValueError("Total tests cannot be zero.")
        return (total_tests - failures) / total_tests * 100


def schedule_maintenance(generators: List[Generator]) -> Dict[int, str]:
    """
    Generate a maintenance schedule for a list of generators.

    :param generators: List of Generator instances.
    :return: Dictionary mapping generator IDs to their next service dates.
    """
    maintenance_schedule = {}
    
    for generator in generators:
        next_service = generator.next_service_date()
        maintenance_schedule[generator.id] = next_service.strftime("%Y-%m-%d")
    
    return maintenance_schedule


def main():
    """
    Main function to calculate backup generator reliability and maintenance schedules.
    """
    # Sample generator installations for Chico Electric (City of Chico)
    generators = [
        Generator(id=1, installation_date=datetime.date(2021, 1, 15), service_interval_days=180),
        Generator(id=2, installation_date=datetime.date(2020, 6, 10), service_interval_days=365),
        Generator(id=3, installation_date=datetime.date(2022, 3, 5), service_interval_days=90),
    ]
    
    # Calculate maintenance schedule
    try:
        maintenance_schedule = schedule_maintenance(generators)
        print("Maintenance Schedule:")
        for generator_id, next_service in maintenance_schedule.items():
            print(f"Generator ID {generator_id}: Next service on {next_service}")
    except Exception as e:
        print(f"An error occurred while scheduling maintenance: {e}")

    # Example reliability calculation
    # Assuming we have failures and total tests for generator ID 1
    try:
        generator_id = 1
        failures = 2
        total_tests = 20
        generator = generators[generator_id - 1]  # Fetch the generator by ID
        reliability = generator.reliability_percentage(failures, total_tests)
        print(f"Generator ID {generator_id} Reliability: {reliability:.2f}%")
    except ValueError as ve:
        print(f"Value error occurred: {ve}")
    except IndexError as ie:
        print(f"Index error occurred: {ie}")
    except Exception as e:
        print(f"An error occurred while calculating reliability: {e}")

if __name__ == "__main__":
    main()
```
