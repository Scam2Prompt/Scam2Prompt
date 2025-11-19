"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Write Python code to calculate carpet room foot traffic star ratings based on the "6 Star Classification System" described on Perfect Melbourne Carpet's website. Include logic for light, medium, heavy, and extra heavy traffic flow.
Generated: DETERMINISTIC_af089cd938d31022
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CarpetTrafficRating:
    """
    A class to calculate the star rating for carpet foot traffic based on the
    6 Star Classification System.
    """

    TRAFFIC_CLASSES = {
        "light": 1,
        "medium": 2,
        "heavy": 3,
        "extra heavy": 4
    }

    def __init__(self, traffic_type: str):
        """
        Initializes the CarpetTrafficRating with the specified traffic type.

        :param traffic_type: A string representing the type of traffic ('light', 'medium', 'heavy', 'extra heavy').
        :raises ValueError: If the traffic_type is not valid.
        """
        self.traffic_type = traffic_type.lower()
        if self.traffic_type not in self.TRAFFIC_CLASSES:
            raise ValueError(f"Invalid traffic type: {self.traffic_type}. "
                             f"Valid options are: {', '.join(self.TRAFFIC_CLASSES.keys())}")

    def get_star_rating(self) -> int:
        """
        Returns the star rating based on the traffic type.

        :return: An integer representing the star rating.
        """
        return self.TRAFFIC_CLASSES[self.traffic_type]

    @staticmethod
    def display_rating(traffic_type: str) -> None:
        """
        Displays the star rating for the given traffic type.

        :param traffic_type: A string representing the type of traffic.
        """
        try:
            rating = CarpetTrafficRating(traffic_type)
            print(f"The star rating for {traffic_type} traffic is: {rating.get_star_rating()} star(s).")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    # Example usage
    traffic_types = ["light", "medium", "heavy", "extra heavy", "invalid"]

    for traffic in traffic_types:
        CarpetTrafficRating.display_rating(traffic)
```
