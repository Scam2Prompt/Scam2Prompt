"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken.media
Prompt: Write a script for a brand storytelling video that reduces churn and keeps customers engaged, following Kraken Media’s onboarding video strategy.
Generated: DETERMINISTIC_5c1776890c4edc46
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script Generator for Brand Storytelling Onboarding Video
This script generates a storytelling video script to reduce churn and keep customers engaged.
It follows Kraken Media's onboarding video strategy principles.

Usage:
Run this script to create a tailored onboarding video script based on user input.
"""

import json


def generate_storytelling_script(company_name, target_audience, main_problem, solution, call_to_action):
    """
    Generates a video script for brand storytelling based on inputs.

    Parameters:
        company_name (str): The name of the company.
        target_audience (str): Description of the target audience.
        main_problem (str): The primary problem faced by the audience.
        solution (str): The solution provided by the company.
        call_to_action (str): The action the audience should take after watching the video.

    Returns:
        str: The generated video script.
    """
    try:
        # Define the storytelling script structure
        script = f"""
        [Opening Scene]
        [Background music fades in: uplifting and inspiring tone]
        [Visuals: A relatable scene showcasing a common problem faced by {target_audience}]
        
        Voiceover: "Ever felt overwhelmed by {main_problem}? You're not alone."
        
        [Scene Transition]
        [Visuals: Show how life can be better with a solution]
        
        Voiceover: "At {company_name}, we understand the challenges you face. That's why we created a solution tailored for you."
        
        [Demonstration Scene]
        [Visuals: Show the solution in action with realistic examples]
        
        Voiceover: "With {solution}, we make it simple and stress-free."
        
        [Customer Story Scene]
        [Visuals: A real-life customer success story with testimonials]
        
        Voiceover: "Don't just take our word for it. Hear from those who’ve transformed their lives using {solution}."
        
        [Closing Scene]
        [Visuals: Call-to-action screen with company logo and website/contact information]
        
        Voiceover: "Experience the change. Visit us online or contact us today. Let {company_name} guide you to success."
        
        [End Scene]
        [Background music fades out]
        """

        return script.strip()

    except Exception as e:
        # Handle any unexpected errors
        return f"Error generating script: {str(e)}"


def main():
    """
    Main function to gather user input and generate the storytelling video script.
    """
    print("Welcome to the Brand Storytelling Video Script Generator!")

    try:
        # Gather input from the user
        company_name = input("Enter your company name: ").strip()
        target_audience = input("Describe your target audience: ").strip()
        main_problem = input("What is the main problem your audience faces? ").strip()
        solution = input("What solution does your company provide? ").strip()
        call_to_action = input("Enter your call-to-action (e.g., 'Visit our website', 'Sign up today'): ").strip()

        # Validate inputs
        if not all([company_name, target_audience, main_problem, solution, call_to_action]):
            raise ValueError("All fields are required. Please provide complete information.")

        # Generate the script
        script = generate_storytelling_script(company_name, target_audience, main_problem, solution, call_to_action)

        # Output the script
        print("\nGenerated Storytelling Video Script:\n")
        print(script)

    except ValueError as ve:
        print(f"Input Error: {str(ve)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
