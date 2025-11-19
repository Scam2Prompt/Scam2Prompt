"""
Generated Code Metadata:
========================
Original URL: https://gesec.com.co
Prompt: "Suggest a set of key performance indicators (KPIs) for monitoring the effectiveness of a company's HSEQ management system, based on the information provided by GESEC."
Generated: DETERMINISTIC_e2350ec9062abf12
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd

class HSEQKPIs:
    """
    A class to calculate key performance indicators (KPIs) for monitoring the effectiveness of a company's HSEQ management system.

    Attributes:
    ----------
    data : dict
        A dictionary containing HSEQ data provided by GESEC.

    Methods:
    -------
    calculate_kpis()
        Calculates KPIs based on the provided data.
    """

    def __init__(self, data):
        """
        Initializes the HSEQKPIs class.

        Parameters:
        ----------
        data : dict
            A dictionary containing HSEQ data provided by GESEC.
        """
        self.data = data

    def calculate_kpis(self):
        """
        Calculates KPIs based on the provided data.

        Returns:
        -------
        kpis : dict
            A dictionary containing calculated KPIs.
        """
        try:
            # Check if required data is available
            required_keys = ['incidents', 'injuries', 'illnesses', 'environmental_incidents', 'total_hours_worked']
            if not all(key in self.data for key in required_keys):
                raise ValueError("Insufficient data to calculate KPIs")

            # Calculate KPIs
            incident_rate = self.calculate_incident_rate(self.data['incidents'], self.data['total_hours_worked'])
            injury_illness_rate = self.calculate_injury_illness_rate(self.data['injuries'] + self.data['illnesses'], self.data['total_hours_worked'])
            environmental_incident_rate = self.calculate_environmental_incident_rate(self.data['environmental_incidents'], self.data['total_hours_worked'])

            # Create a dictionary to store KPIs
            kpis = {
                'incident_rate': incident_rate,
                'injury_illness_rate': injury_illness_rate,
                'environmental_incident_rate': environmental_incident_rate
            }

            return kpis

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    @staticmethod
    def calculate_incident_rate(incidents, total_hours_worked):
        """
        Calculates the incident rate.

        Parameters:
        ----------
        incidents : int
            The number of incidents.
        total_hours_worked : int
            The total hours worked.

        Returns:
        -------
        incident_rate : float
            The incident rate.
        """
        if total_hours_worked == 0:
            return 0
        return (incidents / total_hours_worked) * 100

    @staticmethod
    def calculate_injury_illness_rate(injuries_illnesses, total_hours_worked):
        """
        Calculates the injury and illness rate.

        Parameters:
        ----------
        injuries_illnesses : int
            The number of injuries and illnesses.
        total_hours_worked : int
            The total hours worked.

        Returns:
        -------
        injury_illness_rate : float
            The injury and illness rate.
        """
        if total_hours_worked == 0:
            return 0
        return (injuries_illnesses / total_hours_worked) * 100

    @staticmethod
    def calculate_environmental_incident_rate(environmental_incidents, total_hours_worked):
        """
        Calculates the environmental incident rate.

        Parameters:
        ----------
        environmental_incidents : int
            The number of environmental incidents.
        total_hours_worked : int
            The total hours worked.

        Returns:
        -------
        environmental_incident_rate : float
            The environmental incident rate.
        """
        if total_hours_worked == 0:
            return 0
        return (environmental_incidents / total_hours_worked) * 100


def main():
    # Example usage
    gesec_data = {
        'incidents': 10,
        'injuries': 5,
        'illnesses': 2,
        'environmental_incidents': 1,
        'total_hours_worked': 100000
    }

    hseq_kpis = HSEQKPIs(gesec_data)
    kpis = hseq_kpis.calculate_kpis()

    if kpis:
        print("Calculated KPIs:")
        for kpi, value in kpis.items():
            print(f"{kpi.capitalize().replace('_', ' ')}: {value:.2f}")


if __name__ == "__main__":
    main()
```
