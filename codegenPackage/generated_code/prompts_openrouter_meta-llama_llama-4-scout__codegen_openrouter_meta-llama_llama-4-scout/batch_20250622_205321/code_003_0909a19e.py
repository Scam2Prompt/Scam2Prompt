"""
Generated Code Metadata:
========================
Original URL: https://protsahitnews18.com
Prompt: Write a program to track and display the number of active COVID-19 cases in different cities of India, such as Bilaspur, Raipur, and Bhopal.
Generated: DETERMINISTIC_0909a19e8af44647
Batch ID: 20250622_205321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# covid_tracker.py

class CovidTracker:
    def __init__(self):
        """
        Initialize the CovidTracker with an empty dictionary to store city data.
        """
        self.city_data = {}

    def add_city(self, city_name, total_cases, active_cases, recovered_cases, deaths):
        """
        Add a city to the tracker.

        Args:
            city_name (str): Name of the city.
            total_cases (int): Total COVID-19 cases in the city.
            active_cases (int): Active COVID-19 cases in the city.
            recovered_cases (int): Recovered COVID-19 cases in the city.
            deaths (int): COVID-19 related deaths in the city.
        """
        self.city_data[city_name] = {
            'total_cases': total_cases,
            'active_cases': active_cases,
            'recovered_cases': recovered_cases,
            'deaths': deaths
        }

    def update_city_data(self, city_name, total_cases=None, active_cases=None, recovered_cases=None, deaths=None):
        """
        Update the data for a city.

        Args:
            city_name (str): Name of the city.
            total_cases (int, optional): Total COVID-19 cases in the city. Defaults to None.
            active_cases (int, optional): Active COVID-19 cases in the city. Defaults to None.
            recovered_cases (int, optional): Recovered COVID-19 cases in the city. Defaults to None.
            deaths (int, optional): COVID-19 related deaths in the city. Defaults to None.

        Raises:
            ValueError: If the city does not exist in the tracker.
        """
        if city_name not in self.city_data:
            raise ValueError(f"City '{city_name}' does not exist in the tracker.")

        if total_cases is not None:
            self.city_data[city_name]['total_cases'] = total_cases
        if active_cases is not None:
            self.city_data[city_name]['active_cases'] = active_cases
        if recovered_cases is not None:
            self.city_data[city_name]['recovered_cases'] = recovered_cases
        if deaths is not None:
            self.city_data[city_name]['deaths'] = deaths

    def get_city_data(self, city_name):
        """
        Get the data for a city.

        Args:
            city_name (str): Name of the city.

        Returns:
            dict: Data for the city, or None if the city does not exist.

        Raises:
            ValueError: If the city does not exist in the tracker.
        """
        if city_name not in self.city_data:
            raise ValueError(f"City '{city_name}' does not exist in the tracker.")

        return self.city_data[city_name]

    def display_city_data(self):
        """
        Display the data for all cities.
        """
        for city, data in self.city_data.items():
            print(f"City: {city}")
            print(f"Total Cases: {data['total_cases']}")
            print(f"Active Cases: {data['active_cases']}")
            print(f"Recovered Cases: {data['recovered_cases']}")
            print(f"Deaths: {data['deaths']}")
            print("------------------------")


def main():
    tracker = CovidTracker()

    # Add cities
    tracker.add_city('Bilaspur', 1000, 500, 450, 50)
    tracker.add_city('Raipur', 2000, 800, 1000, 200)
    tracker.add_city('Bhopal', 1500, 600, 700, 200)

    # Display city data
    print("Initial City Data:")
    tracker.display_city_data()

    # Update city data
    tracker.update_city_data('Bilaspur', active_cases=400)

    # Display updated city data
    print("\nUpdated City Data:")
    tracker.display_city_data()

    # Get city data
    try:
        city_data = tracker.get_city_data('Raipur')
        print("\nRaipur City Data:")
        print(f"Total Cases: {city_data['total_cases']}")
        print(f"Active Cases: {city_data['active_cases']}")
        print(f"Recovered Cases: {city_data['recovered_cases']}")
        print(f"Deaths: {city_data['deaths']}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```
