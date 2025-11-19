"""
Generated Code Metadata:
========================
Original URL: https://koltinsuchitoto.com
Prompt: Write a script to generate customer reviews for a hostel, incorporating elements like cleanliness, location, and service quality, as highlighted in the testimonials for Hostal Koltin Suchitoto.
Generated: DETERMINISTIC_4e400082262cad86
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Review:
    """Class to represent a customer review for a hostel."""
    
    def __init__(self, cleanliness, location, service_quality):
        self.cleanliness = cleanliness
        self.location = location
        self.service_quality = service_quality

    def generate_review(self):
        """Generate a formatted review string based on the attributes."""
        return (f"Review:\n"
                f"Cleanliness: {self.cleanliness}\n"
                f"Location: {self.location}\n"
                f"Service Quality: {self.service_quality}\n"
                f"Overall Experience: {self.get_overall_experience()}\n")

    def get_overall_experience(self):
        """Determine the overall experience based on the ratings."""
        average_rating = (self.cleanliness + self.location + self.service_quality) / 3
        if average_rating >= 4.5:
            return "Excellent"
        elif average_rating >= 3.5:
            return "Good"
        elif average_rating >= 2.5:
            return "Average"
        else:
            return "Poor"

def generate_random_review():
    """Generate a random review with ratings for cleanliness, location, and service quality."""
    cleanliness = random.uniform(1, 5)
    location = random.uniform(1, 5)
    service_quality = random.uniform(1, 5)
    
    return Review(cleanliness, location, service_quality)

def main():
    """Main function to generate and display multiple customer reviews."""
    num_reviews = 5  # Number of reviews to generate
    reviews = []

    for _ in range(num_reviews):
        review = generate_random_review()
        reviews.append(review.generate_review())

    # Print all generated reviews
    print("\n".join(reviews))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
