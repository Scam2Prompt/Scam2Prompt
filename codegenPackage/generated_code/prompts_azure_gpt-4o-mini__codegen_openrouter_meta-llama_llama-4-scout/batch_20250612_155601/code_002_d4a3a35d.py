"""
Generated Code Metadata:
========================
Original URL: https://shivvedika.com
Prompt: Create a library function that automates the scheduling of traditional Hindu rituals and ceremonies, inspired by the services provided by Shiv Vedika.
Generated: DETERMINISTIC_d4a3a35df55e6472
Batch ID: 20250612_155601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
import math

class HinduRitualScheduler:
    """
    A library for scheduling traditional Hindu rituals and ceremonies.
    """

    def __init__(self):
        # Initialize an empty dictionary to store rituals
        self.rituals = {}

    def add_ritual(self, name, date, time, duration):
        """
        Add a ritual to the scheduler.

        Args:
            name (str): The name of the ritual.
            date (str): The date of the ritual in YYYY-MM-DD format.
            time (str): The time of the ritual in HH:MM format.
            duration (int): The duration of the ritual in minutes.

        Raises:
            ValueError: If the date or time is not in the correct format.
        """
        try:
            ritual_date = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
            self.rituals[name] = {
                "date": ritual_date,
                "duration": timedelta(minutes=duration)
            }
        except ValueError as e:
            raise ValueError("Invalid date or time format") from e

    def get_ritual_schedule(self, date=None):
        """
        Get the schedule of rituals for a given date or all rituals if no date is provided.

        Args:
            date (str, optional): The date for which to retrieve the ritual schedule in YYYY-MM-DD format. Defaults to None.

        Returns:
            dict: A dictionary of rituals with their dates and durations.
        """
        if date:
            try:
                ritual_date = datetime.strptime(date, "%Y-%m-%d").date()
                return {name: details for name, details in self.rituals.items() if details["date"].date() == ritual_date}
            except ValueError as e:
                raise ValueError("Invalid date format") from e
        return self.rituals

    def calculate_panchang(self, date):
        """
        Calculate the Panchang for a given date.

        Args:
            date (str): The date for which to calculate the Panchang in YYYY-MM-DD format.

        Returns:
            dict: A dictionary containing the Panchang details.
        """
        try:
            panchang_date = datetime.strptime(date, "%Y-%m-%d")
            # Calculate Tithi
            tithi = self.calculate_tithi(panchang_date)
            # Calculate Nakshatra
            nakshatra = self.calculate_nakshatra(panchang_date)
            # Calculate Yoga
            yoga = self.calculate_yoga(panchang_date)
            # Calculate Karana
            karana = self.calculate_karana(panchang_date)
            # Calculate Paksha
            paksha = self.calculate_paksha(panchang_date)

            return {
                "tithi": tithi,
                "nakshatra": nakshatra,
                "yoga": yoga,
                "karana": karana,
                "paksha": paksha
            }
        except ValueError as e:
            raise ValueError("Invalid date format") from e

    @staticmethod
    def calculate_tithi(date):
        # Calculate the Tithi based on the date
        # This is a simplified calculation and actual calculation may be more complex
        tithi_days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        tithi_index = date.timetuple().tm_yday % 15
        tithi_names = ["Purnima", "Waning", "Waning", "Waning", "Waning", "Waning", "Waning", "Amavasya", "Waxing", "Waxing", "Waxing", "Waxing", "Waxing", "Waxing", "Waxing"]
        return tithi_names[tithi_index]

    @staticmethod
    def calculate_nakshatra(date):
        # Calculate the Nakshatra based on the date
        # This is a simplified calculation and actual calculation may be more complex
        nakshatra_names = ["Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra", "Punarvasu", "Pushya", "Ashadha", "Shravana", "Dhanishta", "Shataataraka", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"]
        nakshatra_index = math.floor((date.timetuple().tm_yday * 24 * 60 / 840) % 27)
        return nakshatra_names[nakshatra_index]

    @staticmethod
    def calculate_yoga(date):
        # Calculate the Yoga based on the date
        # This is a simplified calculation and actual calculation may be more complex
        yoga_names = ["Vishkambha", "Pratabda", "Sadhya", "Shruma", "Druva", "Aadaya", "Basu", "Maha", "Vriddha", "Dhruva", "Vyatipada", "Harisarman"]
        yoga_index = math.floor((date.timetuple().tm_yday * 24 * 60 / 1080) % 27)
        return yoga_names[yoga_index]

    @staticmethod
    def calculate_karana(date):
        # Calculate the Karana based on the date
        # This is a simplified calculation and actual calculation may be more complex
        karana_names = ["Kinstughna", "Bava", "Balava", "Kaulava", "Taisatra", "Gara", "Vanija", "Vishti", "Sakuni", "Chatuur", "Nansu", "Kitu"]
        karana_index = math.floor((date.timetuple().tm_yday * 24 * 60 / 720) % 11)
        return karana_names[karana_index]

    @staticmethod
    def calculate_paksha(date):
        # Calculate the Paksha based on the date
        # This is a simplified calculation and actual calculation may be more complex
        if date.timetuple().tm_mday < 15:
            return "Waxing"
        else:
            return "Waning"


def main():
    scheduler = HinduRitualScheduler()
    scheduler.add_ritual("Puja", "2024-09-16", "06:00", 60)
    scheduler.add_ritual("Havan", "2024-09-17", "07:00", 90)

    print("Ritual Schedule:")
    for ritual, details in scheduler.get_ritual_schedule().items():
        print(f"{ritual}: {details['date']} - {details['date'] + details['duration']}")

    print("\nPanchang for 2024-09-16:")
    print(scheduler.calculate_panchang("2024-09-16"))


if __name__ == "__main__":
    main()
```
