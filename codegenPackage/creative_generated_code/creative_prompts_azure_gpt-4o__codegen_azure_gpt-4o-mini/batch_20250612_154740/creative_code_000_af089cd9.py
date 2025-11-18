"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Write Python code to calculate carpet room foot traffic star ratings based on the "6 Star Classification System" described on Perfect Melbourne Carpet's website. Include logic for light, medium, heavy, and extra heavy traffic flow.
Generated: DETERMINISTIC_af089cd938d31022
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CarpetTrafficStarRating:
    """
    A class to calculate the star rating for carpet traffic flow based on the
    6 Star Classification System for different levels of foot traffic.
    """

    TRAFFIC_LEVELS = {
        "light": 1,
        "medium": 2,
        "heavy": 3,
        "extra heavy": 4
    }

    def __init__(self, traffic_flow):
        """
        Initializes the CarpetTrafficStarRating with the given traffic flow.

        :param traffic_flow: str - The level of traffic flow: 'light', 'medium', 'heavy', or 'extra heavy'.
        :raises ValueError: If the provided traffic flow level is invalid.
        """
        self.traffic_flow = traffic_flow.lower()
        if self.traffic_flow not in self.TRAFFIC_LEVELS:
            raise ValueError(f"Invalid traffic flow level: {self.traffic_flow}. "
                             "Choose from 'light', 'medium', 'heavy', 'extra heavy'.")

    def get_star_rating(self):
        """
        Calculates the star rating based on the traffic flow level.

        :return: int - The star rating corresponding to the traffic flow level.
        """
        return self.TRAFFIC_LEVELS[self.traffic_flow]

def main():
    """
    Main function to demonstrate the CarpetTrafficStarRating class.
    It captures user input and displays the corresponding star rating.
    """
    try:
        traffic_flow = input("Enter the traffic flow (light, medium, heavy, extra heavy): ")
        rating = CarpetTrafficStarRating(traffic_flow)
        print(f"The star rating for '{traffic_flow}' traffic is: {rating.get_star_rating()} stars.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
