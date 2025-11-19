"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vaarabella.com
Prompt: Develop a script that automates the display of customer testimonials for a clothing brand, similar to the reviews featured on Vaarabella's website.
Generated: DETERMINISTIC_d98faef33737e719
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

# List to store customer testimonials
testimonials = [
    {
        "name": "Alice Johnson",
        "testimonial": "Absolutely love the quality of the clothes. The designs are so trendy!",
        "rating": 5
    },
    {
        "name": "Mark Smith",
        "testimonial": "Great customer service and fast shipping. Highly recommend.",
        "rating": 4
    },
    {
        "name": "Sophia Lee",
        "testimonial": "The fit is perfect, and the material feels so premium. Very satisfied!",
        "rating": 5
    },
    {
        "name": "James Brown",
        "testimonial": "Decent clothing, but I expected quicker delivery. Overall good experience.",
        "rating": 3
    },
    {
        "name": "Emma Davis",
        "testimonial": "Amazing products! I get compliments every time I wear them.",
        "rating": 5
    },
]

def display_testimonial(testimonial):
    """
    Function to display a customer testimonial in a formatted manner.
    :param testimonial: A dictionary containing testimonial details
    """
    print("\n" + "-" * 50)
    print(f"Customer Name: {testimonial['name']}")
    print(f"Testimonial: {testimonial['testimonial']}")
    print(f"Rating: {'⭐' * testimonial['rating']} ({testimonial['rating']} out of 5)")
    print("-" * 50)

def main():
    """
    Main function to automate the display of customer testimonials.
    Testimonials are displayed one at a time in a loop, with a delay between each.
    """
    print("Welcome to [Clothing Brand]! Here's what our customers have to say:\n")
    
    try:
        while True:  # Infinite loop to continuously display testimonials
            # Randomly pick a testimonial to display
            testimonial = random.choice(testimonials)
            display_testimonial(testimonial)

            # Wait for 5 seconds before showing the next testimonial
            time.sleep(5)
    except KeyboardInterrupt:
        # Graceful exit when user interrupts the script (Ctrl+C)
        print("\nThank you for viewing our testimonials. Have a great day!")

if __name__ == "__main__":
    # Entry point of the script
    main()
```
