"""
Generated Code Metadata:
========================
Original URL: https://zircuitzrc.com
Prompt: What are the key factors to consider when selecting a residential cleaning service, and how do they impact the quality of cleaning?
Generated: DETERMINISTIC_3ccc814d017d29f8
Batch ID: 20250622_210033
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# residential_cleaning_service_selector.py

class ResidentialCleaningService:
    def __init__(self, name, price, reviews, services_offered, equipment_used, staff_experience):
        """
        Initialize a ResidentialCleaningService object.

        Args:
            name (str): The name of the cleaning service.
            price (float): The price of the cleaning service.
            reviews (list): A list of reviews from previous customers.
            services_offered (list): A list of services offered by the cleaning service.
            equipment_used (list): A list of equipment used by the cleaning service.
            staff_experience (int): The average experience of the cleaning staff in years.
        """
        self.name = name
        self.price = price
        self.reviews = reviews
        self.services_offered = services_offered
        self.equipment_used = equipment_used
        self.staff_experience = staff_experience

    def calculate_quality_score(self):
        """
        Calculate a quality score for the cleaning service based on its factors.

        Returns:
            float: A quality score between 0 and 1.
        """
        # Calculate a score based on the number of services offered
        services_score = len(self.services_offered) / 10

        # Calculate a score based on the staff experience
        experience_score = self.staff_experience / 10

        # Calculate a score based on the price
        price_score = 1 / (self.price / 100)

        # Calculate a score based on the reviews
        if len(self.reviews) == 0:
            reviews_score = 0
        else:
            reviews_score = sum(1 for review in self.reviews if review >= 4) / len(self.reviews)

        # Calculate the overall quality score
        quality_score = (services_score + experience_score + price_score + reviews_score) / 4

        return quality_score


def select_cleaning_service(services):
    """
    Select the best residential cleaning service based on its quality score.

    Args:
        services (list): A list of ResidentialCleaningService objects.

    Returns:
        ResidentialCleaningService: The best residential cleaning service.

    Raises:
        ValueError: If the input list is empty.
    """
    if len(services) == 0:
        raise ValueError("The input list cannot be empty")

    # Calculate the quality score for each service
    quality_scores = {service: service.calculate_quality_score() for service in services}

    # Select the service with the highest quality score
    best_service = max(quality_scores, key=quality_scores.get)

    return best_service


def main():
    try:
        # Create some example cleaning services
        service1 = ResidentialCleaningService(
            "Service 1",
            100,
            [4, 5, 3],
            ["dusting", "vacuuming", "mopping"],
            ["vacuum", "mop"],
            5
        )

        service2 = ResidentialCleaningService(
            "Service 2",
            120,
            [5, 5, 4],
            ["dusting", "vacuuming", "mopping", "windows"],
            ["vacuum", "mop", "ladder"],
            10
        )

        service3 = ResidentialCleaningService(
            "Service 3",
            80,
            [3, 4, 4],
            ["dusting", "vacuuming"],
            ["vacuum"],
            2
        )

        # Select the best cleaning service
        services = [service1, service2, service3]
        best_service = select_cleaning_service(services)

        # Print the best cleaning service
        print(f"Best cleaning service: {best_service.name}")
        print(f"Quality score: {best_service.calculate_quality_score():.2f}")
        print(f"Price: ${best_service.price:.2f}")
        print(f"Services offered: {', '.join(best_service.services_offered)}")
        print(f"Equipment used: {', '.join(best_service.equipment_used)}")
        print(f"Staff experience: {best_service.staff_experience} years")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
