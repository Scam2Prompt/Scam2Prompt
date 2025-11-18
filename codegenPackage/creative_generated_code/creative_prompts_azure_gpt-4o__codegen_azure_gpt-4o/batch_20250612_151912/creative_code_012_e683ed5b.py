"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://majeli-avocats.com
Prompt: Write Python code to analyze and categorize client reviews for Majeli Avocat based on keywords like "divorce," "adoption," "homoparental family," and "criminal defense."
Generated: DETERMINISTIC_e683ed5b5ecfebf1
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def categorize_reviews(reviews):
    """
    Analyzes and categorizes client reviews based on predefined keywords.
    
    Parameters:
        reviews (list of str): A list of client reviews (strings).
        
    Returns:
        dict: A dictionary where keys are categories and values are lists of reviews
              that fall under each category.
    """
    # Define keywords for each category
    categories = {
        "Divorce": ["divorce", "separation", "custody"],
        "Adoption": ["adoption", "foster care", "child placement"],
        "Homoparental Family": ["homoparental", "same-sex parents", "lgbtq family"],
        "Criminal Defense": ["criminal defense", "crime", "trial", "court", "law enforcement"]
    }

    # Initialize the result dictionary
    categorized_reviews = {category: [] for category in categories}

    # Process each review
    for review in reviews:
        # Determine if the review matches any of the categories
        for category, keywords in categories.items():
            # Check if any keyword is present in the review text (case-insensitive)
            if any(re.search(rf"\b{keyword}\b", review, re.IGNORECASE) for keyword in keywords):
                categorized_reviews[category].append(review)
                break  # Assign to one category only, then stop further checks

    return categorized_reviews


# Example usage
if __name__ == "__main__":
    # Sample list of client reviews
    sample_reviews = [
        "The lawyer helped us with our divorce and custody arrangements.",
        "We were very happy with how they handled the adoption process.",
        "As a homoparental family, we appreciated the firm's expertise in LGBTQ matters.",
        "Their criminal defense team was highly professional during the trial.",
        "I needed support with my separation, and they were very responsive.",
        "The firm truly understands the challenges facing same-sex parents."
    ]

    try:
        # Analyze and categorize the reviews
        categorized_reviews = categorize_reviews(sample_reviews)
        
        # Display the results
        print("Categorized Reviews:")
        for category, reviews in categorized_reviews.items():
            print(f"\n{category} ({len(reviews)} reviews):")
            for review in reviews:
                print(f"- {review}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")
```
