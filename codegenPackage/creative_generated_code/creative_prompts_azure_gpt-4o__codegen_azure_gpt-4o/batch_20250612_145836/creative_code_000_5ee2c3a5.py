"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://comestim.com.co
Prompt: Write a Python script to simulate a customer satisfaction survey for an edible printing service, including fields for rating product quality and user experience.
Generated: DETERMINISTIC_5ee2c3a5bb9fd695
Batch ID: 20250612_145836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def collect_customer_survey():
    """
    Collects customer satisfaction survey input for an edible printing service.
    Includes fields for product quality and user experience ratings.
    """
    print("Welcome to the Edible Printing Service Satisfaction Survey!")
    print("We value your feedback. Please answer the following questions.")
    print("Note: Ratings are on a scale of 1 (Poor) to 5 (Excellent).\n")

    try:
        # Collect product quality feedback
        product_quality = int(input("How would you rate the product quality? (1-5): "))
        if product_quality < 1 or product_quality > 5:
            raise ValueError("Rating must be between 1 and 5.")

        # Collect user experience feedback
        user_experience = int(input("How would you rate your overall user experience? (1-5): "))
        if user_experience < 1 or user_experience > 5:
            raise ValueError("Rating must be between 1 and 5.")

        # Collect additional comments
        additional_comments = input("Do you have any additional comments? (Optional): ").strip()

        # Create a dictionary with survey results
        survey_results = {
            "Product Quality": product_quality,
            "User Experience": user_experience,
            "Additional Comments": additional_comments
        }

        # Save results to a JSON file
        with open("customer_survey_results.json", "w") as file:
            json.dump(survey_results, file, indent=4)

        print("\nThank you for your feedback! Your responses have been recorded.")

    except ValueError as ve:
        print(f"Input Error: {ve}. Please restart the survey and provide valid ratings.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please try again later.")

if __name__ == "__main__":
    collect_customer_survey()
```
