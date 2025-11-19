"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koltinsuchitoto.com
Prompt: Write a script to generate customer reviews for a hostel, incorporating elements like cleanliness, location, and service quality, as highlighted in the testimonials for Hostal Koltin Suchitoto.
Generated: DETERMINISTIC_4e400082262cad86
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def generate_review():
    """
    Generate a random customer review for a hostel based on criteria 
    such as cleanliness, location, and service quality.
    
    Returns:
        str: A complete, formatted review.
    """
    # Define review elements
    cleanliness_comments = [
        "The rooms were spotless and very well-maintained.",
        "Cleanliness was top-notch, I felt very comfortable.",
        "Impeccable cleanliness, truly impressive!"
    ]
    
    location_comments = [
        "The location was perfect, close to all the main attractions.",
        "A beautiful spot in the heart of Suchitoto, very convenient.",
        "Great location with stunning views of the town."
    ]
    
    service_comments = [
        "The staff were incredibly friendly and helpful.",
        "Service quality exceeded my expectations, truly amazing!",
        "Everyone was attentive and made sure my stay was special."
    ]
    
    # Define overall impressions
    overall_impressions = [
        "Highly recommend this hostel to anyone visiting Suchitoto!",
        "Absolutely loved my stay, would definitely come back!",
        "One of the best hostel experiences I've ever had."
    ]
    
    # Randomly select elements for the review
    cleanliness = random.choice(cleanliness_comments)
    location = random.choice(location_comments)
    service = random.choice(service_comments)
    overall = random.choice(overall_impressions)
    
    # Combine elements into a full review
    review = f"{cleanliness} {location} {service} {overall}"
    return review

def main():
    """
    Main function to generate and display customer reviews.
    """
    try:
        # Number of reviews to generate
        num_reviews = int(input("Enter the number of reviews to generate: "))
        
        if num_reviews <= 0:
            print("Please enter a positive number.")
            return
        
        # Generate and display reviews
        print("\nGenerated reviews:")
        for i in range(num_reviews):
            print(f"Review {i + 1}: {generate_review()}")
    
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
