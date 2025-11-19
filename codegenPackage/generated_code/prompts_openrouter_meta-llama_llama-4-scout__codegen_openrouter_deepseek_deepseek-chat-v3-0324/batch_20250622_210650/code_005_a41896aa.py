"""
Generated Code Metadata:
========================
Original URL: https://happyscholarsacademy.com
Prompt: Write a script for a parent testimonial about their experience with Happy Scholars Academy, highlighting its strengths and positive impact on their child's development.
Generated: DETERMINISTIC_a41896aa96cccf3c
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Parent Testimonial Generator for Happy Scholars Academy
This script generates a heartfelt testimonial highlighting the positive impact
of Happy Scholars Academy on a child's development.
"""

import random
from datetime import datetime

class TestimonialGenerator:
    """
    Generates personalized parent testimonials for Happy Scholars Academy.
    """
    
    def __init__(self):
        self.child_name = ""
        self.parent_name = ""
        self.child_age = 0
        self.enrollment_duration = ""
        self.strengths = [
            "exceptional academic program",
            "nurturing environment",
            "dedicated teachers",
            "holistic approach to education",
            "focus on character development",
            "innovative teaching methods",
            "small class sizes",
            "emphasis on creativity",
            "strong community values",
            "personalized attention"
        ]
        self.improvements = [
            "academic performance",
            "social skills",
            "confidence",
            "creativity",
            "problem-solving abilities",
            "independence",
            "love for learning",
            "communication skills",
            "emotional intelligence",
            "critical thinking"
        ]
    
    def get_user_input(self):
        """Collects necessary information from the user."""
        print("Welcome to the Happy Scholars Academy Testimonial Generator!")
        print("Please provide some details about your experience:\n")
        
        self.child_name = input("Your child's name: ").strip()
        self.parent_name = input("Your name: ").strip()
        self.child_age = input(f"{self.child_name}'s age: ").strip()
        self.enrollment_duration = input("How long has your child attended? (e.g., '6 months', '2 years'): ").strip()
        
        print("\nSelect up to 3 strengths of the academy that stood out to you:")
        for i, strength in enumerate(self.strengths, 1):
            print(f"{i}. {strength}")
        
        selected_indices = input("\nEnter numbers separated by commas (e.g., 1,3,5): ").strip().split(',')
        self.selected_strengths = [self.strengths[int(i)-1] for i in selected_indices if i.isdigit()]
        
        print("\nSelect up to 3 areas where your child showed improvement:")
        for i, improvement in enumerate(self.improvements, 1):
            print(f"{i}. {improvement}")
        
        selected_indices = input("\nEnter numbers separated by commas (e.g., 2,4,6): ").strip().split(',')
        self.selected_improvements = [self.improvements[int(i)-1] for i in selected_indices if i.isdigit()]
    
    def generate_testimonial(self):
        """Generates a personalized testimonial based on user input."""
        if not all([self.child_name, self.parent_name, self.child_age, self.enrollment_duration]):
            raise ValueError("Missing required information for testimonial generation")
        
        strengths_phrase = ", ".join(self.selected_strengths[:-1]) + f", and {self.selected_strengths[-1]}" if len(self.selected_strengths) > 1 else self.selected_strengths[0]
        improvements_phrase = ", ".join(self.selected_improvements[:-1]) + f", and {self.selected_improvements[-1]}" if len(self.selected_improvements) > 1 else self.selected_improvements[0]
        
        testimonial = f"""
        Testimonial for Happy Scholars Academy
        
        Date: {datetime.now().strftime('%B %d, %Y')}
        
        As a parent of {self.child_name} (age {self.child_age}), I can't express enough how grateful we are 
        for the {strengths_phrase} at Happy Scholars Academy. 
        
        In the {self.enrollment_duration} that {self.child_name} has attended, we've seen remarkable growth 
        in their {improvements_phrase}. The teachers and staff genuinely care about each child's 
        development and create an environment where children thrive both academically and socially.
        
        What sets Happy Scholars Academy apart is their ability to make learning engaging while 
        instilling important values. {self.child_name} wakes up excited to go to school every day, 
        and that enthusiasm for learning is priceless.
        
        I wholeheartedly recommend Happy Scholars Academy to any parent looking for an exceptional 
        educational experience for their child. It's been transformative for our family.
        
        Sincerely,
        {self.parent_name}
        """
        
        return testimonial
    
    def save_testimonial(self, testimonial):
        """Saves the generated testimonial to a file."""
        filename = f"happy_scholars_testimonial_{datetime.now().strftime('%Y%m%d')}.txt"
        try:
            with open(filename, 'w') as f:
                f.write(testimonial)
            print(f"\nTestimonial saved successfully as {filename}")
        except IOError as e:
            print(f"\nError saving testimonial: {e}")

def main():
    """Main function to execute the testimonial generation process."""
    try:
        generator = TestimonialGenerator()
        generator.get_user_input()
        testimonial = generator.generate_testimonial()
        print("\n" + "="*50)
        print(testimonial)
        print("="*50 + "\n")
        
        save_choice = input("Would you like to save this testimonial? (yes/no): ").strip().lower()
        if save_choice == 'yes':
            generator.save_testimonial(testimonial)
        
        print("\nThank you for sharing your experience with Happy Scholars Academy!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please try again or contact support.")

if __name__ == "__main__":
    main()
```
