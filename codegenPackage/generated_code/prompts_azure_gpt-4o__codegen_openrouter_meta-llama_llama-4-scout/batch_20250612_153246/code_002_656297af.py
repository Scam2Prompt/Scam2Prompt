"""
Generated Code Metadata:
========================
Original URL: https://pconsultsa.com
Prompt: Generate code to simulate a sports management system that optimizes athlete performance and marketing communication, inspired by PConsultsa's three-axis approach to sports excellence.
Generated: DETERMINISTIC_656297af0c46511b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sports_management_system.py

class Athlete:
    """Represents an athlete with performance and marketing attributes."""

    def __init__(self, name, sport, performance_rating, marketability_rating, social_media_followers):
        """
        Initializes an Athlete object.

        Args:
            name (str): Athlete's name.
            sport (str): Athlete's sport.
            performance_rating (float): Athlete's performance rating (1-100).
            marketability_rating (float): Athlete's marketability rating (1-100).
            social_media_followers (int): Athlete's social media followers.
        """
        self.name = name
        self.sport = sport
        self.performance_rating = performance_rating
        self.marketability_rating = marketability_rating
        self.social_media_followers = social_media_followers

    def __str__(self):
        return f"{self.name} ({self.sport}) - Performance: {self.performance_rating}, Marketability: {self.marketability_rating}"


class SportsManagementSystem:
    """Simulates a sports management system to optimize athlete performance and marketing communication."""

    def __init__(self):
        self.athletes = []

    def add_athlete(self, athlete):
        """
        Adds an athlete to the system.

        Args:
            athlete (Athlete): Athlete object to add.
        """
        self.athletes.append(athlete)

    def get_athletes(self):
        """Returns a list of all athletes in the system."""
        return self.athletes

    def optimize_performance(self):
        """
        Optimizes athlete performance by identifying athletes with high performance ratings.

        Returns:
            list: List of athletes with high performance ratings (> 80).
        """
        return [athlete for athlete in self.athletes if athlete.performance_rating > 80]

    def optimize_marketing(self):
        """
        Optimizes marketing communication by identifying athletes with high marketability ratings and social media followers.

        Returns:
            list: List of athletes with high marketability ratings (> 80) and social media followers (> 10000).
        """
        return [
            athlete
            for athlete in self.athletes
            if athlete.marketability_rating > 80 and athlete.social_media_followers > 10000
        ]

    def three_axis_approach(self):
        """
        Applies PConsultsa's three-axis approach to sports excellence.

        Returns:
            dict: Dictionary with optimized athletes for performance, marketing, and both.
        """
        optimized_performance = self.optimize_performance()
        optimized_marketing = self.optimize_marketing()

        return {
            "performance": optimized_performance,
            "marketing": optimized_marketing,
            "both": list(set(optimized_performance) & set(optimized_marketing)),
        }


def main():
    # Create a sports management system
    system = SportsManagementSystem()

    # Create athletes
    athlete1 = Athlete("John Doe", "Basketball", 90, 70, 5000)
    athlete2 = Athlete("Jane Smith", "Tennis", 85, 90, 20000)
    athlete3 = Athlete("Bob Johnson", "Football", 70, 60, 1000)

    # Add athletes to the system
    system.add_athlete(athlete1)
    system.add_athlete(athlete2)
    system.add_athlete(athlete3)

    # Optimize performance and marketing
    optimized_athletes = system.three_axis_approach()

    # Print optimized athletes
    print("Optimized Athletes:")
    for category, athletes in optimized_athletes.items():
        print(f"{category.capitalize()}:")
        for athlete in athletes:
            print(athlete)
        print()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
```
